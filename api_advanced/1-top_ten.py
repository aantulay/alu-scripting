#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "alu-scripting:api-advanced:v1.0 (by /u/alu_user)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print("None")
