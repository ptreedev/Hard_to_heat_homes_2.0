import json
from src.variables import OS_KEY
from src.variables import OS_ROOF_URL, OS_KEY
from src.os_api import os_roof_api_call

HEADERS = {"Accept": "application/json"}
PARAMS = {
        "key": OS_KEY,
        "limit": 3,
         }

def test_get_api_response():

    data = os_roof_api_call(HEADERS, PARAMS)

    with open("roof_data.json", "w") as f:
        json.dump(data, f, indent=4)
    assert True