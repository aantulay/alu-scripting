#!/usr/bin/python3
"""
Module to recursively count keywords in hot article titles from Reddit.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively queries Reddit and prints a sorted count of given keywords."""
    if counts is None:
        counts = {}
        # Normalize keyword list to lowercase for case-insensitive matching
        word_list = [word.lower() for word in word_list]

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api-advanced:v1.0 (by /u/alu_user)"}
    params = {"after": after} if after else {}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        # Split title into words using spaces to avoid partial matches (e.g. java.)
        title_words = title.split()
        for word in word_list:
            matches = title_words.count(word)
            if matches > 0:
                counts[word] = counts.get(word, 0) + matches

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    # Base case / final recursion reached: sort and print results
    if not counts:
        return

    # Sort by count descending, then alphabetically ascending
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print("{}: {}".format(word, count))
