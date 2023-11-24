#!/usr/bin/python3
import json
import requests

LIMIT_PER_PAGE = 100

def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "count": count, "limit": LIMIT_PER_PAGE}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
        results = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    results_data = results.get("data")
    after = results_data.get("after")
    count += results_data.get("dist")

    for c in results_data.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                instances[word] = instances.get(word, 0) + times

    if after is None:
        if not instances:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)

