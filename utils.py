import requests
from config import POLE_EMPLOI_CLIENT_ID, POLE_EMPLOI_CLIENT_SECRET, POLE_EMPLOI_TOKEN_URL

def obtenir_token():
    data = {
        "client_id": POLE_EMPLOI_CLIENT_ID,
        "client_secret": POLE_EMPLOI_CLIENT_SECRET,
        "grant_type": "client_credentials",
        "scope": "api_offresdemploiv2 o2dsoffre"
    }
    response = requests.post(POLE_EMPLOI_TOKEN_URL, data=data)
    response.raise_for_status()
    return response.json()["access_token"]
