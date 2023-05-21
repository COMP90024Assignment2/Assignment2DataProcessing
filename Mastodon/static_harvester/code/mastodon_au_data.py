import requests
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json

def stream_federated_timeline_given_hashtag(access_token, hashtag):
    URL = "https://mastodon.au/api/v1/timelines/tag/{}".format(hashtag)
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

if __name__ == "__main__":
    access_token = "riNvzdIeoXoyopIOsUonmVqHf6kLUsl21sOHzW2-9M0"  
    
    mortgage_keywords = ["mortgage", "pledge", "hypothec", "guaranty", "pawn"]
    homeless_keywords = ["homeless", "tramp", "vagrant",'dispossessed', 'unhoused']
    rent_keywords = ["rent", "chummage", "rental",'lease', 'renting', 'leasing', 'tenants']
    income_keywords = ["income", "earning",'payroll', 'paycheque', 'paycheck']

    kw_dicts=[mortgage_keywords,homeless_keywords,rent_keywords,income_keywords]
    file_names=["mastodonau_mortgage_data.json","mastodonau_homeless_data.json",
                "mastodonau_rent_data.json","mastodonau_income_data.json" ]

    for i in range(4):
        keywords=kw_dicts[i]
        output_file='./json_file/'+file_names[i]
        results = []
        for keyword in keywords:
            data = stream_federated_timeline_given_hashtag(access_token, keyword)
            results.extend(data)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)



   