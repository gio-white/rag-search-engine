import os

from collections import defaultdict
from pickle import dump
from lib.search_utils import CACHE_PATH, load_movies

class InvertedIndex:
    def __init__(self) -> None:
        self.index = defaultdict(set)
        self.docmap: dict[int, dict] = {}
        self.index_path = os.path.join(CACHE_PATH, "index.pkl")
        self.docmap_path = os.path.join(CACHE_PATH, "docmap.pkl")

    def __add_document(self, doc_id, text):
        tokens = text.lower().split()
        for token in tokens:
            self.index[token].add(doc_id)

    def get_documents(self, term):
        if self.index.get(term) is None:
            return []
        return sorted(self.index[term.lower()])

    def build(self):
        movies = load_movies()
        for movie in movies:
            self.docmap[movie["id"]] = movie
            self.__add_document(movie["id"], f"{movie['title']} {movie['description']}")

    def save(self):
        os.makedirs(CACHE_PATH, exist_ok=True)

        with open(self.index_path, "wb") as f:
            dump(self.index, f)

        with open(self.docmap_path, "wb") as f:
            dump(self.docmap, f)
