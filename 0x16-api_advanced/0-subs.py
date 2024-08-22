#!/usr/bin/python3
"""
Script to fetch the number of subscribers for a specific Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the subscriber count for a specific subreddit or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            return 0
    except requests.RequestException:
        return 0