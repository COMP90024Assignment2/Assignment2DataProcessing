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
    csv_file_path = 'income_2021.csv'
    json_file_path = 'income_2021.json'

    data = csv_to_json(csv_file_path)
    write_json_file(json_file_path, data)
