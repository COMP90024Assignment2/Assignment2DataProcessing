import json

# List of JSON files to be merged
json_files = ["aussocial_homeless_data.json", "mastodonau_homeless_data.json", "theblower_homeless_data.json"]

data = []
for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data.extend(json.load(f))  # Adds the data from the current file to the list

# Write the combined data to a new file
with open("combined_homeless_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
# Input file
input_file = "combined_homeless_data.json"

data = []
with open(input_file, "r", encoding="utf-8") as f:
    all_data = json.load(f)
    for item in all_data:
        id_value = item.get("id", None)
        created_at_value = item.get("created_at", None)
        if id_value and created_at_value:
            data.append({"id": id_value, "created_at": created_at_value})
import pandas as pd
df = pd.DataFrame(data)
df['created_at'] = pd.to_datetime(df['created_at'])
df['created_at'] = df['created_at'].dt.strftime('%Y.%m.%d')
df_count = df.groupby('created_at').size().reset_index(name='homeless_count')
json_files = ["aussocial_mortgage_data.json", "mastodonau_mortgage_data.json", "theblower_mortgage_data.json"]

data = []
for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data.extend(json.load(f))  # Adds the data from the current file to the list

# Write the combined data to a new file
with open("combined_mortgage_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
    input_file = "combined_mortgage_data.json"

data = []
with open(input_file, "r", encoding="utf-8") as f:
    all_data = json.load(f)
    for item in all_data:
        id_value = item.get("id", None)
        created_at_value = item.get("created_at", None)
        if id_value and created_at_value:
            data.append({"id": id_value, "created_at": created_at_value})
df_1 = pd.DataFrame(data)
df_1['created_at'] = pd.to_datetime(df_1['created_at'])
df_1['created_at'] = df_1['created_at'].dt.strftime('%Y.%m.%d')
df_count_1 = df_1.groupby('created_at').size().reset_index(name='mortgage_count')
json_files = ["aussocial_rent_data.json", "mastodonau_rent_data.json", "theblower_rent_data.json"]

data = []
for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data.extend(json.load(f))  # Adds the data from the current file to the list

# Write the combined data to a new file
with open("combined_rent_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
    input_file = "combined_rent_data.json"

data = []
with open(input_file, "r", encoding="utf-8") as f:
    all_data = json.load(f)
    for item in all_data:
        id_value = item.get("id", None)
        created_at_value = item.get("created_at", None)
        if id_value and created_at_value:
            data.append({"id": id_value, "created_at": created_at_value})
df_2 = pd.DataFrame(data)
df_2['created_at'] = pd.to_datetime(df_2['created_at'])
df_2['created_at'] = df_2['created_at'].dt.strftime('%Y.%m.%d')
df_count_2 = df_2.groupby('created_at').size().reset_index(name='rent_count')

json_files = ["aussocial_income_data.json", "mastodonau_income_data.json", "theblower_income_data.json"]

data = []
for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data.extend(json.load(f))  # Adds the data from the current file to the list

# Write the combined data to a new file
with open("combined_income_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
    input_file = "combined_income_data.json"

data = []
with open(input_file, "r", encoding="utf-8") as f:
    all_data = json.load(f)
    for item in all_data:
        id_value = item.get("id", None)
        created_at_value = item.get("created_at", None)
        if id_value and created_at_value:
            data.append({"id": id_value, "created_at": created_at_value})
df_3 = pd.DataFrame(data)
df_3['created_at'] = pd.to_datetime(df_3['created_at'])
df_3['created_at'] = df_3['created_at'].dt.strftime('%Y.%m.%d')
df_count_3 = df_3.groupby('created_at').size().reset_index(name='income_count')
df_combined = pd.concat([df_count, df_count_1, df_count_2, df_count_3], ignore_index=True)
df_combined_new = df_combined.sort_values('created_at')

# Replace NaN values with 0
df_new = df_combined_new.fillna(0)
df_combined_new = df_combined.sort_values('created_at')

# Replace NaN values with 0
df_new = df_combined_new.fillna(0)
df_new.to_csv('mastodon data.csv', index=False)
import json, csv

def csv_to_json(csv_file_path):
    data = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def write_json_file(json_file_path, data):
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
        
if __name__ == '__main__':
    csv_file_path = 'mastodon data.csv'
    json_file_path = 'mastodon data.json'

    data = csv_to_json(csv_file_path)
    write_json_file(json_file_path, data)