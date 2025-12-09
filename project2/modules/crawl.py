import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawl_urls(urls):
    data = []

    for url in urls:
        try:
            # Request dengan User-Agent supaya tidak diblok Cloudflare
            r = requests.get(url, timeout=10, headers={
                "User-Agent": "Mozilla/5.0"
            })
            soup = BeautifulSoup(r.text, "html.parser")

            # ============================
            # 1️⃣ Ambil artikel utama NativeIndonesia
            # ============================
            content_div = soup.find("div", class_="td-post-content")

            if content_div:
                article = content_div.get_text(" ", strip=True)
            else:
                # fallback 1: cari div lain
                article = soup.get_text(" ", strip=True)

            # ============================
            # 2️⃣ Jika teks terlalu pendek → fallback terakhir
            # ============================
            if len(article) < 150:
                art_tag = soup.find("article")
                if art_tag:
                    article = art_tag.get_text(" ", strip=True)

            data.append({
                "url": url,
                "content": article
            })

        except Exception as e:
            data.append({
                "url": url,
                "content": ""
            })

    return pd.DataFrame(data)
