from lib.preprocessing import preprocessing
from nltk.stem import PorterStemmer

def find_match(query: str, titles: list[str]) -> list[str]:
    query_words = preprocessing(query).split()
    
    with open("data/stopwords.txt","r", encoding="utf-8") as f:
        stopwords_data = f.read()
    
    stopwords = set(stopwords_data.splitlines())
    query_tokens = set(query_words) - stopwords
    
    stemmer = PorterStemmer()
    stemmed_query_tokens = {stemmer.stem(token) for token in query_tokens}
    matches = []

    for title in titles:
        title_tokens = set(preprocessing(title).split()) - stopwords
        stemmed_title_tokens = {stemmer.stem(token) for token in title_tokens}
        if any(qw in tw for qw in stemmed_query_tokens for tw in stemmed_title_tokens):
            matches.append(title)
    
    return matches
