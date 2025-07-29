from tests.test_data.epc_dummy_data import epc_dummy_data
from src.epc_api import epc_api_call
from src.variables import EPC_TOKEN
import pytest

QUERY_PARAMS = "uprn=200002791&uprn=100061342030"
HEADERS = {"Accept": "application/json", "Authorization": f"Basic {EPC_TOKEN}"}

@pytest.fixture
def mock_api_call(mocker):
    mock_get = mocker.patch("src.epc_api.requests.get")
    mock_response = mock_get.return_value
    mock_response.json.return_value = epc_dummy_data
    result = epc_api_call(HEADERS, QUERY_PARAMS)
    return result

def test_get_request_is_called_once(mocker):
    mock_get = mocker.patch("src.epc_api.requests.get")
    mock_response = mock_get.return_value
    mock_response.json.return_value = epc_dummy_data
    result = epc_api_call(HEADERS, QUERY_PARAMS)
    assert result == epc_dummy_data
    mock_get.assert_called_once()

def test_get_request_invalid_uprn(mocker):
    mock_get = mocker.patch("src.epc_api.requests.get")
    mock_response = mock_get.return_value
    mock_response.json.return_value = {}
    result = epc_api_call(HEADERS, "uprn=123456789")
    assert result == {}

def test_not_200_response():
    assert epc_api_call({}, QUERY_PARAMS) == False


def test_result_is_JSON(mock_api_call):
    assert mock_api_call == epc_dummy_data


def test_dummy_data_address(mock_api_call):
    assert mock_api_call["rows"][0]["address"] == epc_dummy_data["rows"][0]["address"]
    assert mock_api_call["rows"][0]["address"] == "30 Alexandra Road, Muswell Hill"


def test_dummy_data_epc_rating(mock_api_call):
    assert (
        mock_api_call["rows"][0]["current-energy-rating"]
        == epc_dummy_data["rows"][0]["current-energy-rating"]
    )
    assert mock_api_call["rows"][0]["current-energy-rating"] == "D"


def test_dummy_data_epc_score(mock_api_call):
    print(f'{mock_api_call["rows"]}')
    assert (
        mock_api_call["rows"][0]["current-energy-efficiency"]
        == epc_dummy_data["rows"][0]["current-energy-efficiency"]
    )
    assert mock_api_call["rows"][0]["current-energy-efficiency"] == "63"