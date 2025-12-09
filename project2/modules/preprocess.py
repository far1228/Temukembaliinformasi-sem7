import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def preprocess(text):
    """Cleaning + normalisasi + stemming."""
    if not isinstance(text, str):
        text = str(text)

    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return stemmer.stem(text).strip()
