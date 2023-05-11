from mpi4py import MPI
import json
import math
import time
import os
import pandas as pd
from collections import Counter
from collections import defaultdict
import re
bad_json = []

import json
import re

def extract_usefull(input_string: str):
    author_id_pattern = r'"author_id"\s*:\s*"(\d+)"'
    full_name_pattern = r'"full_name"\s*:\s*"([^"]+)"'
    input_string += "  }"
    if input_string[0] == ',':
        input_string = input_string[1:]

    author_id = re.search(author_id_pattern, input_string)
    full_name = re.search(full_name_pattern, input_string)

    if author_id and full_name:
        return author_id.group(1), full_name.group(1)
    else:
        return None, None

def process_twitter_data(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as f:
        with open(output_file, "w", encoding="utf-8") as output_f:
            output_f.write("[\n")

            current_twitter_json = ""
            first_output = True
            
            while True:
                try:
                    current_line = f.readline()
                    print(current_line)
                    if current_line == "]\n":
                        break
                    elif current_line == "  },\n" or current_line == "  }\n":
                        
                        if "ability" in current_twitter_json.lower():
                            author_id, full_name = extract_usefull(current_twitter_json)
                            if author_id and full_name:
                                output_dict = {
                                    "author_id": author_id,
                                    "full_name": full_name
                                }
                                if not first_output:
                                    output_f.write(",\n")
                                else:
                                    first_output = False
                                json.dump(output_dict, output_f)
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