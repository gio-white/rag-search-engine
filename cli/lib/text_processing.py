import string
from nltk.stem import PorterStemmer
from lib.search_utils import load_stopwords

def preprocess_text(text:str) -> str:
    text = text.lower()
    translation_map = str.maketrans({k: None for k in string.punctuation})
    text = text.translate(translation_map)
    return text

def tokenize_text(text: str) -> list[str]:
    text = preprocess_text(text)
    tokens = text.split()
    valid_tokens = []
    for token in tokens:
        if token:
            valid_tokens.append(token)
    stop_words = load_stopwords()
    filtered_words = []
    for word in valid_tokens:
        if word not in stop_words:
            filtered_words.append(word)
    stemmer = PorterStemmer()
    stemmed_words = []
    for word in filtered_words:
        stemmed_words.append(stemmer.stem(word))
    return stemmed_words
