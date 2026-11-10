#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the total number of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api-advanced:v1.0 (by /u/alu_user)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    return 0
