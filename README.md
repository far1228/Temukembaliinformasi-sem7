# IR Wisata Indonesia 🌊🏝️  
_Simple Information Retrieval untuk Destinasi Wisata Indonesia berbasis Streamlit_

Proyek ini adalah aplikasi pencarian (search engine mini) untuk destinasi wisata di Indonesia.  
Aplikasi akan melakukan **crawling** ke beberapa website wisata, melakukan **preprocessing teks** (normalisasi + stemming bahasa Indonesia), lalu membangun model **TF-IDF + cosine similarity** untuk menampilkan hasil pencarian yang paling relevan dalam tampilan kartu yang modern.

---

## ✨ Fitur Utama

- 🕸️ **Web Crawling Otomatis**
  - Mengambil konten artikel dari beberapa URL wisata Indonesia.
  - Menggunakan `requests` + `BeautifulSoup` untuk parsing HTML.
  - Data hasil crawl disimpan dalam bentuk `pandas.DataFrame` (kolom `url`, `content`).

- 🧹 **Preprocessing Teks Bahasa Indonesia**
  - Lowercasing & cleaning karakter non-alfabet.
  - Menghapus spasi berlebih.
  - Stemming Bahasa Indonesia dengan **Sastrawi**.
  - Fungsi utama: `preprocess(text)` di `modules/preprocess.py`.

- 🔍 **Information Retrieval dengan TF-IDF**
  - Membentuk vektor TF-IDF dari kolom `clean_text`.
  - Menggunakan **unigram + bigram** (`ngram_range=(1, 2)`) agar frasa seperti “pantai bali” lebih tertangkap.
  - Menghitung kemiripan dokumen–query menggunakan **cosine similarity**.
  - Mengembalikan ranking dokumen beserta skor dan snippet singkat.
  - Di-handle oleh `build_tfidf` dan fungsi pencarian di `modules/ir_model.py`.

- 🖼️ **UI Modern dengan Streamlit**
  - Tema khusus “soft ocean” di `modules/ui_style.py` (gradien biru–kuning pastel).
  - Tampilan header/banner, kartu hasil, dan tombol “Lihat Destinasi →”.
  - Highlight kata kunci pencarian di judul/deskripsi menggunakan elemen `<mark>`.

---

## 🧱 Teknologi yang Digunakan

- **Python 3.10+**
- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [requests](https://requests.readthedocs.io/)
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/)
- [scikit-learn](https://scikit-learn.org/) – TF-IDF & cosine similarity
- [Sastrawi](https://pypi.org/project/Sastrawi/) – stemming Bahasa Indonesia

---

## 📁 Struktur Proyek

```bash
project-root/
├─ app.py
└─ modules/
   ├─ crawl.py          # Fungsi crawl_urls untuk mengambil konten dari daftar URL
   ├─ preprocess.py     # Fungsi preprocess untuk cleaning + normalisasi + stemming
   ├─ ir_model.py       # Build TF-IDF, cosine similarity, dan ranking dokumen
   ├─ ui_style.py       # CSS kustom untuk tema Streamlit
   └─ __pycache__/      # File cache Python (otomatis, bisa di-ignore)
