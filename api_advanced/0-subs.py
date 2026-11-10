#!/usr/bin/python3
"""
Module to query the number of subscribers for
a given subreddit using Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """Queries Reddit API and returns the total number of subscribers."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0.0 (by /u/dazzy)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        return 0
    except Exception:
        return 0
