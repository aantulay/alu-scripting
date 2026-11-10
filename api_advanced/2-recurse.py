#!/usr/bin/python3
"""
Module to recursively query the Reddit API for all hot article titles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns a list containing titles of all hot articles."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "alu-scripting:api-advanced:v1.0 (by /u/alu_user)"
    }
    params = {"after": after} if after else {}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
