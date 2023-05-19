import requests
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json

def stream_federated_timeline_given_hashtag(access_token, hashtag):
    URL = "https://aus.social/api/v1/timelines/tag/{}".format(hashtag)
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
    access_token = "1OM_w4sjj9sUkAxamkbDU_dSrz2CY3EPMVrDLz2-9NU"  

    mortgage_keywords = ["mortgage", "pledge", "hypothec", "guaranty", "pawn"]
    homeless_keywords = ["homeless", "tramp", "vagrant",'dispossessed', 'unhoused']
    rent_keywords = ["rent", "chummage", "rental",'lease', 'renting', 'leasing', 'tenants']
    income_keywords = ["income", "earning",'payroll', 'paycheque', 'paycheck']

    kw_dicts=[mortgage_keywords,homeless_keywords,rent_keywords,income_keywords]
    file_names=["aussocial_mortgage_data.json","aussocial_homeless_data.json",
                "aussocial_rent_data.json","aussocial_income_data.json" ]

    folder='./json_file'
    if not os.path.exists(folder):
        os.makedirs(folder)

    for i in range(4):
        keywords=kw_dicts[i]
        output_file='./json_file/'+file_names[i]
        results = []
        for keyword in keywords:
            data = stream_federated_timeline_given_hashtag(access_token, keyword)
            results.extend(data)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)


 