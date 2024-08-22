#!/usr/bin/python3
"""Module to fetch subreddit subscriber count"""

import requests

def number_of_subscribers(subreddit):
    """Fetches the number of subscribers for a given subreddit using Reddit API"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0

    return (response.json().get("data").get("subscribers"))
    