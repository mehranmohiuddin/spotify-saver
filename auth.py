import requests
from dotenv import dotenv_values
import sys

def get_bearer_token():
    config = dotenv_values(".env")

    url="https://accounts.spotify.com/api/token"
    client_id = config["CLIENT_ID"]
    client_secrets = config["CLIENT_SECRET"]

    request_body = {
        "grant_type": "client_credentials",
        "client_id": f"{client_id}",
        "client_secret": f"{client_secrets}"
    }

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=request_body, headers=headers)

    if response.status_code == 200:
        return response.json()

    print("unable to get bearer token. exiting program")
    sys.exit(1)
    