import json
import urllib.request
from src.variables import OS_KEY
from src.property import Property

with open("tests/test_data/os_places_dummy_data.json") as data:
    os_places_dummy_data = json.load(data)

def os_places_api_call(uprn):
    endpoint_url = f"https://api.os.uk/search/places/v1/uprn?uprn={uprn}&key={OS_KEY}"
    try:
        with urllib.request.urlopen(urllib.request.Request(endpoint_url, headers={"Accept" : "application/json"})) as response:
            response_body= response.read()
            return json.loads(response_body)

    except Exception:
        return False

def test_returns_dict():
    assert type(os_places_api_call(1)) is dict

def test_valid_uprn():
    assert os_places_api_call(100061342030) == os_places_dummy_data

def test_invalid_uprn_format():
    assert os_places_api_call("a") == False

def test_access_property_address():
    test_property = Property(100061342030)
    response = os_places_api_call(test_property.uprn)
    assert response["results"][0]['DPA']['ADDRESS'] == "13A, WILTON GARDENS, WEST MOLESEY, KT8 1QP"

