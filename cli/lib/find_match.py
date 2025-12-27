from lib.preprocessing import preprocessing

def find_match(query: str, titles: list[str]) -> list[str]:
    query_words = preprocessing(query).split()
    
    return [
        title
        for title in titles
        if any(
            qw in tw
            for qw in query_words
            for tw in preprocessing(title).split()
        )
    ]
