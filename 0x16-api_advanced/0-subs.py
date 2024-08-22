#!/usr/bin/python3
"""Module to fetch subreddit subscriber count"""


def number_of_subscribers(subreddit):
    """Fetches the number of subscribers for a given subreddit using Reddit API"""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)