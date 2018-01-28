import re
import requests
import sys
import json
import sqlite3

class h1don:
    mastodon_host = "mstdn-workers.com"
    client_name = "h1de test cli"
    redirect_uris = "urn:ietf:wg:oauth:2.0:oob"
    scopes = "read write follow"
    client_id = ""
    client_secret = ""
    access_token = ""
    def post_hook(self, URL, post_data):
        print(post_data)
        with requests.session() as client:
            try:
                # print("postdata: " + post_data)
                r = client.post(URL, data=post_data)
                print(r.text)
            except Exception as e:
                print("Exception")
                print(e)
                pass
    def get_LTL_stream(self):
        event = ""
        with requests.Session() as s:
            # s.headers.update({'Authorization': "Bearer "+self.access_token})
            s.stream = True
            res = s.get('https://'+self.mastodon_host+'/api/v1/streaming/public/local')
            for line in res.iter_lines():
                line_str = line.decode('utf-8')
                print("---------------------------------------------------")
                # print(line_str)
                if "event: update" in line_str:
                    event = "update"
                if "event: delete" in line_str:
                    event = "delete"
                if "data: " in line_str:
                    line_str = line_str.lstrip('data: ')
                    post_data = {
                        'event': '',
                        'id': '',
                    }
                    if event == "update":
                        post_data['event'] = "update"
                        post_data['id'] = json.loads(line_str)['id']
                    elif event == "delete":
                        post_data['event'] = "delete"
                        post_data['id'] = line_str
                    print(post_data['event'] + ": " + post_data['id'])
                    con = sqlite3.connect("db.sqlite3")
                    con.row_factory = sqlite3.Row
                    for row in con.execute('SELECT * FROM registr_hookreg'):
                        post_data['secret'] = row['secret']
                        self.post_hook(row['to_url'], post_data)
                        print("url: "+row['to_url']+", user:"+row['username'])
