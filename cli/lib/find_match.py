from lib.text_processing import tokenize_text
from lib.search_utils import load_movies, DEFAULT_SEARCH_LIMIT
from lib.inverted_index import InvertedIndex

def find_match(query: str, idx: InvertedIndex) -> list[dict]:
    query_tokens = tokenize_text(query)
    results = []
    seen_ids = set()

    for token in query_tokens:
        doc_ids = idx.get_documents(token)
        
        for doc_id in doc_ids:
            if doc_id not in seen_ids:
                seen_ids.add(doc_id)
                results.append(idx.docmap[doc_id])
                
                if len(results) >= 5:
                    return results

    return results

    # matches = [index.get(qt) for qt in query_tokens if index.get(qt) is not None]
    # res = []
    # for match in matches:
    #     res.extend(list(match))

    # for movie in sorted(movies, key=lambda movie: movie["id"]):
    #     title = movie["title"]
    #     title_tokens = set(tokenize_text(title))

    #     if any(
    #         qw in tw
    #         for qw in query_tokens
    #         for tw in title_tokens
    #     ):
    #         matches.append(movie)

    #     if len(matches) >= DEFAULT_SEARCH_LIMIT:
    #         break

    # return matches
