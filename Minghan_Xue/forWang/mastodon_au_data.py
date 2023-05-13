import requests
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json
def delete_mastodon_status(status_id, access_token):
    url = "https://mastodon.social/@jionghao/api/v1/statuses/{}".format(status_id)
    headers = {
        "Authorization": "Bearer {}".format(access_token),
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print("Status deleted successfully!")
        print(response.json())
    elif response.status_code == 404:
        print("Status not found. It may have been already deleted or the status ID is incorrect.")
    else:
        print("Error deleting status. HTTP status code: {}".format(response.status_code))
        print(response.text)
def stream_federated_timeline_given_hashtag(access_token, hashtag):
    URL = "https://theblower.au/api/v1/timelines/tag/{}".format(hashtag)
    headers = {
        "Authorization": "Bearer {}".format(access_token),
    }

    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        #print("Get the local timeline successfully!")
        data_list = response.json()
        return data_list
    else:
        if response.status_code == 404:
            print("Failed to get local timeline")
        else:
            print("Error get local timeline. HTTP status code: {}".format(response.status_code))
            print(response.text)
        return []  # return an empty list on failure
def full_text_search(access_token):
    URL = "https://mastodon.au/api/v2/search?q={}".format(keyword)
    headers = {
        "Authorization": "Bearer {}".format(access_token),
    }
    
    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        #print("Get the request text successfully!")
        print(response.json())
    elif response.status_code == 404:
        print("Failed to get the request text")
    else:
        print("Error get the request text. HTTP status code: {}".format(response.status_code))
        print(response.text)
def streaming_Mastodon_timeline():
    pass
if __name__ == "__main__":
    access_token = "Z3wfKjDDfUxzL5Zp9XTCbe0OKBm3EuMI1Y6BeDuEHOM"  
    status_id = "110197044539110917"
    keywords = ["homeless", "tramp", "vagrant"]

    output_file = "mastodonau_homeless_data.json"
    results = []
    for keyword in keywords:
        data = stream_federated_timeline_given_hashtag(access_token, keyword)
        results.extend(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
def streaming_Mastodon_timeline():
    pass
if __name__ == "__main__":
    access_token = "Z3wfKjDDfUxzL5Zp9XTCbe0OKBm3EuMI1Y6BeDuEHOM"  
    status_id = "110197044539110917"
    keywords = ["mortgage", "pledge", "hypothec", "guaranty", "pawn"]

    output_file = "mastodonau_mortgage_data.json"
    results = []
    for keyword in keywords:
        data = stream_federated_timeline_given_hashtag(access_token, keyword)
        results.extend(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
def streaming_Mastodon_timeline():
    pass
if __name__ == "__main__":
    access_token = "Z3wfKjDDfUxzL5Zp9XTCbe0OKBm3EuMI1Y6BeDuEHOM"  
    status_id = "110197044539110917"
    keywords = ["rent", "chummage", "rental"]

    output_file = "mastodonau_rent_data.json"
    results = []
    for keyword in keywords:
        data = stream_federated_timeline_given_hashtag(access_token, keyword)
        results.extend(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
def streaming_Mastodon_timeline():
    pass
if __name__ == "__main__":
    access_token = "Z3wfKjDDfUxzL5Zp9XTCbe0OKBm3EuMI1Y6BeDuEHOM"  
    status_id = "110197044539110917"
    keywords = ["income", "earning"]

    output_file = "mastodonau_income_data.json"
    results = []
    for keyword in keywords:
        data = stream_federated_timeline_given_hashtag(access_token, keyword)
        results.extend(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)