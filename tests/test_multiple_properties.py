from src.epc_api import epc_api_call
from src.property import Property
from dotenv import load_dotenv
import os 
from app import get_props

load_dotenv()

TOKEN = os.getenv('EPC_ENCODED_API_TOKEN')

BASE_URL = 'https://epc.opendatacommunities.org/api/v1/domestic/search?'
HEADERS = {
        'Accept': 'application/json',
        'Authorization': f'Basic {TOKEN}'
    }


def test_returns_two_rows_of_properties():
    array_of_properties = epc_api_call(HEADERS, {'local-authority' :'E09000008', 'size' : '2'})['rows']
    assert len(array_of_properties) == 2

def test_returns_an_array_of_two_property_instances():
    array_of_properties = epc_api_call(HEADERS, {'local-authority' :'E09000008', 'size' : '2'})['rows']
    props = get_props(array_of_properties)
    assert type(props) is list
    assert type(props[0]) is Property
    