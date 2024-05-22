from tests.test_data.epc_dummy_data import epc_dummy_data
from src.epc_api import epc_api_call
import os
from src.property import Property
import json 
from src.variables import EPC_TOKEN

with open("tests/test_data/os_dummy_data.json", "r") as data:
    os_dummy_data = json.load(data)

QUERY_PARAMS = "uprn=200002791"
HEADERS = {"Accept": "application/json", "Authorization": f"Basic {EPC_TOKEN}"}

epc_test_property = epc_api_call(HEADERS, QUERY_PARAMS)["rows"][0]


def test_property_has_uprn():
    dummy_property = Property("200002791")
    assert dummy_property.uprn == "200002791"


def test_property_has_uprn_from_dummy_data():
    dummy_property = Property(epc_dummy_data["rows"][0]["uprn"])
    assert dummy_property.uprn == "200002791"


def test_property_has_uprn_from_api_call():
    dummy_property = Property(epc_test_property["uprn"])
    assert dummy_property.uprn == "200002791"


def test_property_has_EPC_rating():
    dummy_property = Property("200002791")
    dummy_property.epc_rating = "D"
    assert dummy_property.epc_rating == "D"


def test_property_has_correct_attributes_from_api_call():
    dummy_property = Property(
        epc_test_property["uprn"]
    )
    dummy_property.epc_rating = "D"
    dummy_property.uprn = "200002791"
    dummy_property.epc_score = "63"
    dummy_property.address = "30 Alexandra Road, Muswell Hill, N10 2RT"
    assert dummy_property.epc_rating == "D"
    assert dummy_property.uprn == "200002791"
    assert dummy_property.epc_score == "63"
    assert dummy_property.address == "30 Alexandra Road, Muswell Hill, N10 2RT"

os_dummy_building = os_dummy_data["features"][0]["properties"]
dummy_property = Property(os_dummy_building["uprnreference"][0]["uprn"])
def test_property_has_uprn_from_os_api():
    assert dummy_property.uprn == 100061342030

def test_property_has_relevant_data_from_os_api():
    dummy_property.age = '1945-1959'
    dummy_property.connectivity = 'Semi-Connected'
    dummy_property.material = 'Brick Or Block Or Stone'
    assert dummy_property.age == os_dummy_building["buildingage_period"]
    assert dummy_property.connectivity == os_dummy_building["connectivity"]
    assert dummy_property.material == os_dummy_building["constructionmaterial"]
