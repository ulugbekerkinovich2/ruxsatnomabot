import requests
import aiohttp
from data.config import base_url, username, password, university_id
from icecream import ic

async def get_token():
    url = f"{base_url}api/token/"
    body = {
        "username": username,
        "password": password
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=body) as response:
            if response.status == 200 and response.content_type == 'application/json':
                token_data = await response.json()
                return token_data
            else:
                text = await response.text()
                print(f"Unexpected response: {text}")
                raise Exception(f"Failed to get token, status: {response.status}, content-type: {response.content_type}")

def create_profile(token, chat_id_user, first_name_user, last_name_user, phone, username, date):
    url = f"{base_url}create-user-profile/"
    headers = {
        "Authorization": f"Token {token}"
    }
    body = {
        "chat_id_user": chat_id_user,
        "first_name": first_name_user,
        "last_name": last_name_user,
        "pin": 1,
        "phone": phone,
        "username": username,
        "date": date,
        "university_name": int(university_id)
    }
    ic(body)

    response = requests.post(url, json=body, headers=headers)
    # ic(response.content)
    return response
