import json
import pytest
from src.property import Property
from src.os_api import os_places_api_call

with open("tests/test_data/os_places_dummy_data.json") as data:
    os_places_dummy_data = json.load(data)

with open("tests/test_data/os_places_bad_call_dummy_data.json") as data:
    os_places_bad_call_dummy_data = json.load(data)

TEST_UPRN = 100061342030

@pytest.fixture
def mock_os_places_api_response(mocker):
    mock_response = os_places_dummy_data
    mock_get = mocker.patch("src.os_api.requests.get")
    mock_get.return_value.json.return_value = mock_response

    return os_places_api_call(TEST_UPRN)

def test_returns_dictionary(mock_os_places_api_response):
    assert type(mock_os_places_api_response) is dict

def test_valid_uprn(mock_os_places_api_response):
    assert mock_os_places_api_response["results"] == os_places_dummy_data["results"]

def test_invalid_uprn_format(mocker):
    mock_response = os_places_bad_call_dummy_data
    mock_get = mocker.patch("src.os_api.requests.get")
    mock_get.return_value.json.return_value = mock_response
    response = os_places_api_call("a")
    assert response == os_places_bad_call_dummy_data

def test_access_property_address(mock_os_places_api_response):
    assert mock_os_places_api_response["results"][0]['DPA']['ADDRESS'] == "13A, WILTON GARDENS, WEST MOLESEY, KT8 1QP"

def test_assign_property_address_from_uprn(mock_os_places_api_response):
    test_property = Property(100061342030)
    print(test_property, "<--- test-property")
    test_property.address = mock_os_places_api_response["results"][0]['DPA']['ADDRESS']
    assert test_property.address == "13A, WILTON GARDENS, WEST MOLESEY, KT8 1QP"