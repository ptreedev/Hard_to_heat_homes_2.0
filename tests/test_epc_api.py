from tests.test_data.epc_dummy_data import epc_dummy_data
from src.epc_api import epc_api_call
from src.variables import EPC_TOKEN

QUERY_PARAMS = "uprn=200002791&uprn=100061342030"
HEADERS = {"Accept": "application/json", "Authorization": f"Basic {EPC_TOKEN}"}
response_data = epc_api_call(HEADERS, QUERY_PARAMS)

def test_200_response():
    assert type(response_data) is dict


def test_200_response_invalid_uprn():
    assert epc_api_call(HEADERS, "uprn=123456789") == {}


def test_not_200_response():
    assert epc_api_call({}, QUERY_PARAMS) == False


def test_result_is_JSON():
    assert response_data == epc_dummy_data


def test_dummy_data_address():
    assert response_data["rows"][0]["address"] == epc_dummy_data["rows"][0]["address"]
    assert response_data["rows"][0]["address"] == "30 Alexandra Road, Muswell Hill"


def test_dummy_data_epc_rating():
    assert (
        response_data["rows"][0]["current-energy-rating"]
        == epc_dummy_data["rows"][0]["current-energy-rating"]
    )
    assert response_data["rows"][0]["current-energy-rating"] == "D"


def test_dummy_data_epc_score():
    print(f'{response_data["rows"]}')
    assert (
        response_data["rows"][0]["current-energy-efficiency"]
        == epc_dummy_data["rows"][0]["current-energy-efficiency"]
    )
    assert response_data["rows"][0]["current-energy-efficiency"] == "63"
