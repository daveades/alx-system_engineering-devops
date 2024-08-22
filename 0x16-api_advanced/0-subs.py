#!/usr/bin/python3
"""
program to Query Reddit API for number of subscribers for a given subreedit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API
    and returns the number of subscribers for a given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except requests.exceptions.HTTPError:
        return 0
    except requests.exceptions.RequestException:
        return 0
    except Exception:
        return 0
