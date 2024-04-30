from src.epc_dummy_data import epc_dummy_data
from src.epc_api import epc_api_call
import os
from dotenv import load_dotenv
from src.property import Property

load_dotenv()

TOKEN = os.getenv("EPC_ENCODED_API_TOKEN")
QUERY_PARAMS = {"uprn": "200002791"}
HEADERS = {"Accept": "application/json", "Authorization": f"Basic {TOKEN}"}

epc_test_property = epc_api_call(HEADERS, QUERY_PARAMS)["rows"][0]


def test_property_has_uprn():
    dummy_property = Property("200002791", None, None, None, None)
    assert dummy_property.uprn == "200002791"


def test_property_has_uprn_from_dummy_data():
    dummy_property = Property(epc_dummy_data["rows"][0]["uprn"], None, None, None, None)
    assert dummy_property.uprn == "200002791"


def test_property_has_uprn_from_api_call():
    dummy_property = Property(epc_test_property["uprn"], None, None, None, None)
    assert dummy_property.uprn == "200002791"


def test_property_has_EPC_rating():
    dummy_property = Property("200002791", "D", None, None, None)
    assert dummy_property.epc_rating == "D"


def test_property_has_correct_attributes_from_api_call():
    dummy_property = Property(
        epc_test_property["uprn"],
        epc_test_property["current-energy-rating"],
        epc_test_property["current-energy-efficiency"],
        epc_test_property["address"],
        epc_test_property["postcode"],
    )
    assert dummy_property.epc_rating == "D"
    assert dummy_property.uprn == "200002791"
    assert dummy_property.epc_score == "63"
    assert dummy_property.address == "30 Alexandra Road, Muswell Hill, N10 2RT"
