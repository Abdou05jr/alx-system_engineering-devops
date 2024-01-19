#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    try:
        sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                                .format(subreddit),
                                headers={"User-Agent": "My-User-Agent"},
                                allow_redirects=False)
        sub_info.raise_for_status()  # Raises an HTTPError for bad responses

        return sub_info.json().get("data").get("subscribers")

    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0

