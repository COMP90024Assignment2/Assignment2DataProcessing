
import re
bad_json = []

import json
import re


def find_keyword(keywords: list, input_string: str) -> dict:
    result = {}
    for keyword, keywordlist in keywords.items():
        for key in keywordlist:
            if key in input_string.lower():
                result[keyword] = 1
                break
    return result

def extract_usefull(input_string: str):
    author_id_pattern = r'"author_id"\s*:\s*"(\d+)"'
    full_name_pattern = r'"full_name"\s*:\s*"([^"]+)"'
    twitter_id_pattern = r'"_id"\s*:\s*"(\d+)"'
    input_string += "  }"
    if input_string[0] == ',':
        input_string = input_string[1:]

    author_id = re.search(author_id_pattern, input_string)
    full_name = re.search(full_name_pattern, input_string)
    twitter_id = re.search(twitter_id_pattern, input_string)

    if author_id and full_name:
        return author_id.group(1), full_name.group(1), twitter_id.group(1)
    else:
        return None, None, None

def process_twitter_data(input_file: str, output_file: str):
    keywords = {"homeless": ["homeless", "tramp", "vagrant"], "income": ["income", "earning", "salary", "wage"], "rental": ["rent", "chummage", "rental"], "mortgage":["mortgage", "pledge", "hypothec", "guaranty", "pawn"]}

    with open(input_file, "r", encoding="utf-8") as f:
        with open(output_file, "w", encoding="utf-8") as output_f:
            output_f.write("[\n")

            current_twitter_json = ""
            first_output = True
            
            while True:
                try:
                    current_line = f.readline()

                    
                    if current_line == "]\n":
                        break
                    elif current_line == "  },\n" or current_line == "  }\n":

                        result_dict = find_keyword(keywords, current_twitter_json.lower())
                        if result_dict != {}:
                            author_id, full_name, twitter_id = extract_usefull(current_twitter_json)
                            if author_id and full_name:
                                output_dict = {
                                    "author_id": author_id,
                                    "twitter_id": twitter_id,
                                    "full_name": full_name
                                }
                                
                                merged_dict = {**output_dict, **result_dict}
                                if not first_output:
                                    output_f.write(",\n")
                                else:
                                    first_output = False

                                json.dump(merged_dict, output_f)

                        current_twitter_json = ""
                    else:
                        current_twitter_json += current_line

                except Exception as e:
                    pass

            output_f.write("\n]")

if __name__ == "__main__":
    #input_file = "D:/Twitter data/twitter-huge.json"
    #input_file = "small_json_file.json"
    #input_file = "smallTwitter.json"
    input_file = "twitter-data-small.json"
    output_file = "preprocess_homeless_twitterdata.json"
    #output_file = "D:/Twitter data/preprocess_data.json"
    process_twitter_data(input_file, output_file)