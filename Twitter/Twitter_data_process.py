import ijson
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def find_keyword(keywords: dict, input_string: str) -> dict:
    result = {}
    for keyword, keywordlist in keywords.items():
        for key in keywordlist:
            if key in input_string.lower():
                result[keyword] = 1
                break
    return result

def extract_usefull(input_json: dict):
    author_id = input_json.get('doc',{}).get('data', {}).get('author_id')
    full_name = input_json.get('doc',{}).get('includes', {}).get('places', [{}])[0].get('full_name')
    return author_id, full_name

def process_twitter_data(input_file: str, output_file: str):
    keywords = {"homeless": ["homeless", "tramp", "vagrant"], "income": ["income", "earning", "salary", "wage"], "rental": ["rent", "chummage", "rental"], "mortgage":["mortgage", "pledge", "hypothec", "guaranty", "pawn"]}

    with open(input_file, 'rb') as input_f:
        rows = ijson.items(input_f, 'rows.item')
        with open(output_file, "w", encoding="utf-8") as output_f:
            output_f.write("[\n")
            first_output = True
            for obj in rows:
                try:
                    result_dict = find_keyword(keywords, obj.get('doc',{}).get('data', {}).get('text', ''))
                    if result_dict != {}:
                        author_id, full_name = extract_usefull(obj)
                        if author_id and full_name:
                            output_dict = {
                                "author_id": author_id,
                                "full_name": full_name
                            }
                            
                            merged_dict = {**output_dict, **result_dict}
                            if not first_output:
                                output_f.write(",\n")
                            else:
                                first_output = False
                            json.dump(merged_dict, output_f, cls=DecimalEncoder)
                except Exception:
                    pass  # Ignore the error and continue to the next row
            output_f.write("\n]")

if __name__ == "__main__":
    input_file = "D:/Twitter data/twitter-huge.json"
    #input_file = "C:/Users/13008/python/90024AS2/small_json_file.json"
    #input_file = "smallTwitter.json"
    #input_file = "twitter-data-small.json"
    #output_file = "preprocess_homeless_twitterdata.json"
    output_file = "D:/Twitter data/preprocess_homeless_data.json"
    process_twitter_data(input_file, output_file)