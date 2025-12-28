from lib.text_processing import tokenize_text
from lib.search_utils import load_movies, DEFAULT_SEARCH_LIMIT


def find_match(query: str) -> list[dict]:
    query_tokens = set(tokenize_text(query))
    movies = load_movies()
    matches = []

    for movie in sorted(movies, key=lambda movie: movie["id"]):
        title = movie["title"]
        title_tokens = set(tokenize_text(title))

        if any(
            qw in tw
            for qw in query_tokens
            for tw in title_tokens
        ):
            matches.append(movie)
                   
        if len(matches) >= DEFAULT_SEARCH_LIMIT:
            break

    return matches
