from src.epc_api import epc_api_call
from src.property import Property
from dotenv import load_dotenv
import os 

load_dotenv()

TOKEN = os.getenv('EPC_ENCODED_API_TOKEN')

BASE_URL = 'https://epc.opendatacommunities.org/api/v1/domestic/search?'
HEADERS = {
        'Accept': 'application/json',
        'Authorization': f'Basic {TOKEN}'
    }

def get_props(props):
    result = []
    for prop in props:
        result.append(Property(prop['uprn'], prop['current-energy-rating'], prop['current-energy-efficiency'], prop['address'], prop['postcode']))

    # print(f'>>>>>>>{result[0].address}')
    return result


def test_returns_two_rows_of_properties():
    array_of_properties = epc_api_call(HEADERS, {'local-authority' :'E09000008', 'size' : '2'})['rows']
    assert len(array_of_properties) == 2

def test_returns_an_array_of_two_property_instances():
    array_of_properties = epc_api_call(HEADERS, {'local-authority' :'E09000008', 'size' : '2'})['rows']
    props = get_props(array_of_properties)
    assert type(props) is list
    assert type(props[0]) is Property
    