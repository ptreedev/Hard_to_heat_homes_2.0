from tests.test_data.epc_dummy_data import epc_dummy_data
from src.epc_api import epc_api_call
from src.variables import EPC_TOKEN

QUERY_PARAMS = "uprn=200002791&uprn=100061342030"
HEADERS = {"Accept": "application/json", "Authorization": f"Basic {EPC_TOKEN}"}

def test_get_request_is_called_once(mocker):
    mock_get = mocker.patch("src.epc_api.requests.get")
    mock_response = mock_get.return_value
    mock_response.json.return_value = epc_dummy_data
    result = epc_api_call(HEADERS, QUERY_PARAMS)
    assert result == epc_dummy_data
    mock_get.assert_called_once()