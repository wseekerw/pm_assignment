import requests
from posts.utils.config import ROOT_URL

def fetch_users():
    response = requests.get(ROOT_URL + '/users/')
    response.raise_for_status()
    return response.json()