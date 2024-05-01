import urllib.request
from urllib.parse import urlencode
import os
from dotenv import load_dotenv
import json

load_dotenv()


HEADERS = {"Accept": "application/json"}
BASE_URL = "https://api.os.uk/features/ngd/ofa/v1/collections/bld-fts-building-2/items?"
OS_API_KEY = os.getenv("OS_API_KEY")


def os_api_call(headers, params):
    full_url = f"{BASE_URL}{urlencode(params)}"
    try:
        with urllib.request.urlopen(
            urllib.request.Request(full_url, headers=headers)
        ) as response:
            response_body = response.read()
            return json.loads(response_body)

    except Exception:
        return False
    
    
response = os_api_call(HEADERS, {"key": OS_API_KEY, "limit" : 1})


def test_not_200_response():
    assert os_api_call({}, {}) == False


def test_200_response():
    assert type(response) is dict


def test_features_array_is_populated():    
    assert len(response["features"]) > 0
