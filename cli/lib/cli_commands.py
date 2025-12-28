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
    
    idx = InvertedIndex()
    try:
        idx.load()
    except FileNotFoundError:
        print("Error: Index not found. Please run 'build' first.")
        return []

    res = find_match(text, idx)
    
    for item in res:
        print(f"{item['id']}. {item['title']}")

    return res