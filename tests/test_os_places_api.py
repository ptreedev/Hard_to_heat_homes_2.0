import json
from src.property import Property
from src.os_api import os_places_api_call

with open("tests/test_data/os_places_dummy_data.json") as data:
    os_places_dummy_data = json.load(data)


response = os_places_api_call(100061342030)

def test_returns_dict():
    assert type(os_places_api_call(1)) is dict

def test_valid_uprn():
    assert response["results"] == os_places_dummy_data["results"]

def test_invalid_uprn_format():
    assert os_places_api_call("a") == False

def test_access_property_address():
    assert response["results"][0]['DPA']['ADDRESS'] == "13A, WILTON GARDENS, WEST MOLESEY, KT8 1QP"

def test_assign_property_address_from_uprn():
    test_property = Property(100061342030)
    test_property.address = response["results"][0]['DPA']['ADDRESS']
    assert test_property.address == "13A, WILTON GARDENS, WEST MOLESEY, KT8 1QP"