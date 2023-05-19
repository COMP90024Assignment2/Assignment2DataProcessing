import os
import json
import sys
from couchdb import Server

# Provide the CouchDB server's URL, username, and password
couchdb_url = 'http://jionghao:123456@172.26.134.63:5984/'
json_files_directory = './json_file/'

server = Server(couchdb_url)

# Read JSON files and push them to CouchDB
for file in os.listdir(json_files_directory):
    if file.endswith('.json') and file.startswith('combined'):
        db_name=('mastodon_'+file[9:-5])
        if db_name not in server:
            db = server.create(db_name)
        else:
            db = server[db_name]
        with open(os.path.join(json_files_directory, file), 'r') as f:
            data = json.load(f)
            for d in data:
                db.save(d)