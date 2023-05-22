from mastodon import Mastodon, MastodonFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json
import couchdb 

m = Mastodon(
        api_base_url = f'https://mastodon.au'
        access_token = os.environ[]
)

masternode = 
user = 
password = 
url = 'http://'+jionghao+':'+password+'@'+masternode+':5984/'
couchclient = couchdb.Server(url)\

name = "sudo"
couchclient.create(name)
db = couchclient[name]

class Listener(StreamListener):
    def on_update(self, status):
        obj = json.loads(json.dumps(status, indent = 2, sort_keys = True, default=str))
        db.save(obj)

m.stream_public(Listener())

