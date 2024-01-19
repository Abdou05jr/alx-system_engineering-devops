#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
	"""Return the total number of subscribers on a given subreddit."""
	url = "htpps://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {
		"User-Agent": "Linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
	}
	response = request.get(url, headers=headers, allow_redirects=False)
	if response.status_code == 404:
		return 0
	results =response.json().get("data")
	return results.get("subscribers")
