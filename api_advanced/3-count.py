#!/usr/bin/python3
"""
Recursive module to parse hot article titles and count specified keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively queries Reddit API and prints sorted keyword counts."""
    if counts is None:
        counts = {}
        # Normalize keyword list to lowercase for case-insensitive matching
        word_list = [w.lower() for w in word_list]

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0 (by /u/dazzy)"}
    params = {"after": after} if after else {}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])
    after = data.get("after")

    for child in children:
        title = child.get("data", {}).get("title", "").lower()
        # Clean title punctuation to avoid counting words inside punctuation
        words = "".join(
            [c if c.isalnum() or c.isspace() else " " for c in title]
        ).split()
        for word in words:
            if word in word_list:
                counts[word] = counts.get(word, 0) + 1

    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    # Base case reached: print results if any counts exist
    if not counts:
        return

    # Sort by count descending, then alphabetically ascending
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print("{}: {}".format(word, count))
