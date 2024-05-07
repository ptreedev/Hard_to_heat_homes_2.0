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

response = os_places_api_call(100061342030)

def test_returns_dict():
    assert type(os_places_api_call(1)) is dict

def test_valid_uprn():
    assert response == os_places_dummy_data

def test_invalid_uprn_format():
    assert os_places_api_call("a") == False

def test_access_property_address():
    assert response["results"][0]['DPA']['ADDRESS'] == "13A, WILTON GARDENS, WEST MOLESEY, KT8 1QP"

def test_assign_property_address_from_uprn():
    test_property = Property(100061342030)
    test_property.address = response["results"][0]['DPA']['ADDRESS']
    assert test_property.address == "13A, WILTON GARDENS, WEST MOLESEY, KT8 1QP"