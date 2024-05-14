import json
from src.os_api import os_api_call
from src.variables import OS_KEY

with open("tests/test_data/os_dummy_data.json") as data:
    os_dummy_data = json.load(data)

HEADERS = {"Accept": "application/json"}


response = os_api_call(
    HEADERS,
    {
        "key": OS_KEY,
        "limit": 3,
        "filter": "oslandusetiera LIKE 'Residential Accommodation' AND ismainbuilding=true",
        "bbox": "-0.372438,51.405655,-0.371885,51.40600",
    },
)


def test_not_200_response():
    assert os_api_call({}, {}) == False


def test_200_response():
    assert type(response) is dict


def test_features_array_is_populated():
    assert len(response["features"]) > 0

first_building = response["features"][0]["properties"]
def test_one_building_accessing_desired_response_data():
    assert first_building["connectivity"] == "Semi-Connected"
    year = (
        first_building["buildingage_year"]
        if first_building["buildingage_year"]
        else first_building["buildingage_period"]
    )
    assert year == "1945-1959"
    assert first_building["constructionmaterial"] == "Brick Or Block Or Stone"

def test_get_uprns_from_one_building():
    for i in range(len(first_building["uprnreference"])):
        assert first_building["uprnreference"][i]['uprn'] == os_dummy_data["features"][0]["properties"]["uprnreference"][i]["uprn"]


def test_accessing_desired_response_data_for_multiple_buildings():
    for i in range(len(response["features"])):
        response_building = response["features"][i]["properties"]
        response_building_coordinates = response["features"][i]["geometry"]["coordinates"]
        dummy_data_building = os_dummy_data["features"][i]["properties"]
        
        year = "buildingage_year" if response_building["buildingage_year"] else "buildingage_period"
        assert response_building[year] == dummy_data_building[year]
        assert response_building["connectivity"] == dummy_data_building["connectivity"]
        assert response_building["constructionmaterial"] == dummy_data_building["constructionmaterial"]
        assert response_building_coordinates[0] == os_dummy_data["features"][i]["geometry"]["coordinates"][0]
        for j in range(len(response_building["uprnreference"])):
            assert (
                response_building["uprnreference"][j]["uprn"]
                == dummy_data_building["uprnreference"][j]["uprn"]
            )

