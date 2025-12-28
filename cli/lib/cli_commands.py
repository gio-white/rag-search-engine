from lib.inverted_index import InvertedIndex
from lib.find_match import find_match

def build_command() -> None:
    print("Building inverted index...")
    idx = InvertedIndex()
    idx.build()
    idx.save()
    print("Inverted index built successfully.")


def search_command(text) -> list[dict]:
    print(f"Searching for: {text}")
    res = find_match(text)
    for idx, item in enumerate(res):
        print(f"{idx + 1}. {item["title"]}")

    return res
