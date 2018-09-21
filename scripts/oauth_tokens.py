#!/usr/local/bin/python
import requests
import os
import json
import sys
import hcl

def main():
    stdin_json = json.loads(sys.stdin.read())
    atlas_token = stdin_json.get("tfe_token")
    org = stdin_json.get("tfe_org")
    api = stdin_json.get("tfe_api")

    headers = {"Authorization": "Bearer {0}".format(atlas_token)}
 
    resp = requests.get("https://{0}/api/v2/organizations/{1}/oauth-tokens".format(api, org), 
            headers=headers)
    data = resp.json()
    try:
        print json.dumps(dict(oauth_token=data.get("data")[0].get("id")))
    except:
        sys.stderr.write( "Could not find Token. Have you connected your VCS?" )
        
if __name__ == '__main__':
    main()

