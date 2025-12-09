import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_tfidf(df):
    """
    Membangun model TF-IDF dari kolom clean_text.
    Menggunakan ngram agar pencarian bekerja lebih akurat.
    """
    vectorizer = TfidfVectorizer(
        max_features=5000,        # batas fitur
        ngram_range=(1, 2),       # penting! mendukung frasa seperti “pantai bali”
        stop_words=None
    )
    
    matrix = vectorizer.fit_transform(df["clean_text"])
    return vectorizer, matrix



def search_documents(query, df, vectorizer, matrix, preprocess_fn, top_k=5):
    """
    Melakukan pencarian dokumen berdasarkan query.
    """
    # Preprocess query
    q = preprocess_fn(query)
    q_vec = vectorizer.transform([q])

    # Hitung kesamaan cosine
    sim = cosine_similarity(q_vec, matrix).flatten()

    # Urutkan berdasarkan skor tertinggi
    idx = sim.argsort()[::-1][:top_k]

    results = df.iloc[idx].copy()
    results["score"] = sim[idx]

    # Generate snippet ringkas
    results["snippet"] = results["content"].apply(
        lambda t: t[:220] + "..." if isinstance(t, str) and len(t) > 220 else t
    )

    return results
