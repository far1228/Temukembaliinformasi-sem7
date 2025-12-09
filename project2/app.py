import streamlit as st
import pandas as pd
import re

from modules.crawl import crawl_urls
from modules.preprocess import preprocess
import modules.ir_model as irm
from modules.ui_style import inject_css

# === Required ===
st.set_page_config(page_title="IR Wisata Indonesia", layout="wide")
inject_css()

# =======================
# THUMBNAIL LIST
# =======================
def unsplash(url):
    return url + "?auto=format&fit=crop&w=900&q=80"

THUMBNAILS = {
    "bali": unsplash("https://images.unsplash.com/photo-1507525428034-b723cf961d3e"),
    "lombok": unsplash("https://images.unsplash.com/photo-1519821172141-b5d8adf39d35"),
    "jatim": unsplash("https://images.unsplash.com/photo-1501785888041-af3ef285b470"),
    "jogja": unsplash("https://images.unsplash.com/photo-1509679708047-e0e562d21e42"),
    "sumatera": unsplash("https://images.unsplash.com/photo-1554435493-93422f80a18e"),
    "ntt": unsplash("https://images.unsplash.com/photo-1606131731935-481c0a33f3bd"),
    "kalimantan": unsplash("https://images.unsplash.com/photo-1505731132164-cca5cc9f3292"),
}

DEFAULT_IMAGE = THUMBNAILS["bali"]

# =======================
# HEADER
# =======================
st.markdown("<div class='main-title'>Search Engine Wisata Indonesia</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Temukan rekomendasi wisata terbaik di seluruh Indonesia ✨</div>", unsafe_allow_html=True)
st.markdown(f'<img src="{DEFAULT_IMAGE}" class="header-image">', unsafe_allow_html=True)

# =======================
# URL LIST
# =======================
URLS = [
    # ===== BALI =====
    "https://www.nativeindonesia.com/wisata-bali/",
    "https://www.nativeindonesia.com/pantai-kuta-bali/",
    "https://www.nativeindonesia.com/pantai-pandawa-bali/",
    "https://www.nativeindonesia.com/tanah-lot/",
    "https://www.nativeindonesia.com/pura-ulun-danu-beratan/",
    "https://www.nativeindonesia.com/bedugul/",
    "https://www.nativeindonesia.com/nusa-penida/",
    "https://www.nativeindonesia.com/garuda-wisnu-kencana/",
    "https://www.nativeindonesia.com/pantai-sanur/",
    "https://www.nativeindonesia.com/ubud/",
    "https://www.nativeindonesia.com/pantai-melasti-bali/",
    "https://www.nativeindonesia.com/pantai-balangan/",
    "https://www.nativeindonesia.com/pantai-dreamland-bali/",
    "https://www.nativeindonesia.com/pantai-nusa-dua/",
    "https://www.nativeindonesia.com/pantai-green-bowl/",
    
    # ===== LOMBOK =====
    "https://www.nativeindonesia.com/wisata-lombok/",
    "https://www.nativeindonesia.com/pantai-pink-lombok/",
    "https://www.nativeindonesia.com/gunung-rinjani/",
    "https://www.nativeindonesia.com/gili-trawangan/",
    "https://www.nativeindonesia.com/gili-air/",
    "https://www.nativeindonesia.com/gili-meno/",
    "https://www.nativeindonesia.com/bukit-merese/",
    "https://www.nativeindonesia.com/senaru-waterfall-lombok/",
    
    # ===== JAWA TIMUR =====
    "https://www.nativeindonesia.com/gunung-bromo/",
    "https://www.nativeindonesia.com/kawah-ijen/",
    "https://www.nativeindonesia.com/museum-angkut/",
    "https://www.nativeindonesia.com/jatim-park-1/",
    "https://www.nativeindonesia.com/jatim-park-2/",
    "https://www.nativeindonesia.com/jatim-park-3/",
    "https://www.nativeindonesia.com/coban-rondo/",
    "https://www.nativeindonesia.com/coban-rais/",
    "https://www.nativeindonesia.com/selecta-batu/",
    "https://www.nativeindonesia.com/bukit-paralayang-batu/",
    
    # ===== JOGJA =====
    "https://www.nativeindonesia.com/borobudur/",
    "https://www.nativeindonesia.com/prambanan/",
    "https://www.nativeindonesia.com/taman-sari-yogyakarta/",
    "https://www.nativeindonesia.com/gunung-merapi/",
    "https://www.nativeindonesia.com/heha-sky-view/",
    "https://www.nativeindonesia.com/kalibiru/",
    "https://www.nativeindonesia.com/hutan-pinus-mangunan/",
    
    # ===== SUMATERA =====
    "https://www.nativeindonesia.com/danau-toba/",
    "https://www.nativeindonesia.com/air-terjun-sipiso-piso/",
    "https://www.nativeindonesia.com/bukittinggi/",
    "https://www.nativeindonesia.com/jam-gadang/",
    "https://www.nativeindonesia.com/ngarai-sianok/",
    "https://www.nativeindonesia.com/air-terjun-lembah-anai/",
    
    # ===== KALIMANTAN =====
    "https://www.nativeindonesia.com/pulau-derawan/",
    "https://www.nativeindonesia.com/taman-nasional-tanjung-puting/",
    
    # ===== SULAWESI & NTT =====
    "https://www.nativeindonesia.com/bunaken/",
    "https://www.nativeindonesia.com/wakatobi/",
    "https://www.nativeindonesia.com/labuan-bajo/",
    "https://www.nativeindonesia.com/pulau-komodo/",
    "https://www.nativeindonesia.com/pink-beach-komodo/",
]

with st.sidebar:
    st.header("📌 Info Sistem")
    st.write("Total URL:", len(URLS))

# =======================
# LOAD DATA
# =======================
df = crawl_urls(URLS)

# CLEAN TEXT
df["content"] = df["content"].fillna("").astype(str)
df["clean_text"] = df["content"].apply(preprocess)

# BUILD TF-IDF
vectorizer, matrix = irm.build_tfidf(df)

# =======================
# SEARCH INPUT
# =======================
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
query = st.text_input("🔍 Cari destinasi wisata...")
top_k = st.slider("Jumlah hasil", 3, 10, 5)

# =======================
# THUMBNAIL SELECTOR
# =======================
def select_thumbnail(url: str):
    url = url.lower()
    if any(x in url for x in ["bali", "kuta", "pandawa", "ulun"]):
        return THUMBNAILS["bali"]
    return DEFAULT_IMAGE

# =======================
# UTIL FUNCTIONS
# =======================
def clean_url(url):
    return url.rstrip("/")

def highlight(text, query):
    if not text:
        return text
    words = query.lower().split()
    for w in words:
        text = re.sub(fr"({w})", r"<mark>\1</mark>", text, flags=re.IGNORECASE)
    return text

# =======================
# RESULT DISPLAY (UI CARD)
# =======================
if query:
    results = irm.search_documents(query, df, vectorizer, matrix, preprocess, top_k)

    for _, row in results.iterrows():
        thumb = select_thumbnail(row["url"])
        title = row["url"].split("/")[-2].replace("-", " ").title()
        snippet = highlight(row["snippet"], query)
        fixed_url = clean_url(row["url"])

        html = (
            f"<div class='result-card'>"

            f"<div style='position:relative; margin-bottom:16px;'>"
            f"<img src='{thumb}' class='thumb'>"
            f"<div style='position:absolute; top:12px; right:12px; "
            f"background:rgba(255,255,255,0.95); backdrop-filter:blur(8px); "
            f"padding:6px 14px; border-radius:20px; "
            f"font-size:12px; font-weight:700; color:#0284c7; "
            f"box-shadow:0 2px 8px rgba(6, 182, 212, 0.2);'>"
            f"⭐ {row['score']:.2f}</div>"
            f"</div>"

            f"<div style='margin-bottom:10px; font-size:14px; color:#0c4a6e;'>"
            f"📍 Destinasi Wisata Alam Indonesia"
            f"</div>"

            f"<a href='{fixed_url}' target='_blank' "
            f"style='display:block; font-size:22px; font-weight:800; text-decoration:none; "
            f"color:#0c4a6e; margin-bottom:8px; line-height:1.3; "
            f"transition:color 0.2s ease;' "
            f"onmouseover=\"this.style.color='#0284c7'\" "
            f"onmouseout=\"this.style.color='#0c4a6e'\">"
            f"{title}</a>"

            f"<div style='font-size:12px; color:#075985; margin-bottom:14px; opacity:0.8;'>"
            f"🔗 {fixed_url}</div>"

            f"<div style='height:1px; background:linear-gradient(to right, transparent, #67e8f9, #fb923c, transparent); margin:14px 0;'></div>"

            f"<div class='snippet'>"
            f"{snippet}</div>"

            f"<div style='margin-top:16px;'>"
            f"<a href='{fixed_url}' target='_blank' "
            f"style='display:inline-flex; align-items:center; gap:6px; background:linear-gradient(135deg, #67e8f9, #22d3ee); "
            f"color:#0c4a6e; padding:8px 18px; border-radius:10px; text-decoration:none; font-size:13px; font-weight:700; "
            f"transition:all 0.3s ease; box-shadow:0 2px 8px rgba(6, 182, 212, 0.3);' "
            f"onmouseover=\"this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(6, 182, 212, 0.4)'; this.style.background='linear-gradient(135deg, #0ea5e9, #06b6d4)'\" "
            f"onmouseout=\"this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(6, 182, 212, 0.3)'; this.style.background='linear-gradient(135deg, #67e8f9, #22d3ee)'\">"
            f"Lihat Destinasi →</a>"
            f"</div>"

            f"</div>"
        )

        st.markdown(html, unsafe_allow_html=True)