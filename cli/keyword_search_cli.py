#!/usr/bin/env python3

import argparse
import json
from lib.find_match import find_match


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()
    with open("./data/movies.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    movies = data["movies"]

    res = find_match(args.query, [movie["title"] for movie in movies])
    print(res)

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")
            for x in range(min(len(res) -1 ,5)):
                print(f"{x + 1}. {res[x]}")
        case _:
            parser.print_help()




if __name__ == "__main__":
    main()
