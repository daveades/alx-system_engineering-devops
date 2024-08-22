#!/usr/bin/python3
"""
Fetch the number of subscribers for a specified subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API to retrieve the number of subscribers
    (total subscribers, not active users) for a specified subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        
        if response.status_code == 200:
            results = response.json()
            return results.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0