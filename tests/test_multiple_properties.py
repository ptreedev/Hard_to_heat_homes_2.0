from src.epc_api import epc_api_call
from src.property import Property
from dotenv import load_dotenv
import os 
from app import get_props
from tests.test_os_api import os_api_call
import json

with open("src/os_dummy_data.json") as data:
    os_dummy_data = json.load(data)

load_dotenv()

TOKEN = os.getenv('EPC_ENCODED_API_TOKEN')


BASE_URL = 'https://epc.opendatacommunities.org/api/v1/domestic/search?'
HEADERS = {
        'Accept': 'application/json',
        'Authorization': f'Basic {TOKEN}'
    }

OS_API_KEY = os.getenv("OS_API_KEY")
OS_PARAMS = {
        "key": OS_API_KEY,
        "limit": 2,
        "filter": "oslandusetiera LIKE 'Residential Accommodation' AND ismainbuilding=true",
        "bbox": "-0.372438,51.405655,-0.371885,51.40600",
    }


def get_props_from_os(list_of_buildings):
    result = []
    for i in range(len(list_of_buildings)):
        building = list_of_buildings[i]["properties"]
        uprn_array = building["uprnreference"]
        for j in range(len(uprn_array)):
            age = "buildingage_year" if building["buildingage_year"] else "buildingage_period"
            new_prop = Property(uprn_array[j]['uprn'])
            new_prop.connectivity =  building["connectivity"]
            new_prop.age =  building[age]
            new_prop.material =  building["constructionmaterial"]
            result.append(new_prop)
    return result


def test_returns_two_rows_of_properties():
    array_of_properties = epc_api_call(HEADERS, {'local-authority' :'E09000008', 'size' : '2'})['rows']
    assert len(array_of_properties) == 2

def test_returns_an_array_of_two_property_instances():
    array_of_properties = epc_api_call(HEADERS, {'local-authority' :'E09000008', 'size' : '2'})['rows']
    props = get_props(array_of_properties)
    assert type(props) is list
    assert type(props[0]) is Property

def test_returns_multiple_buildings_from_os():
    response = os_api_call({"Accept":"application/json"}, OS_PARAMS)
    array_of_buildings = response["features"]
    assert len(array_of_buildings) > 1
    assert len(os_dummy_data["features"]) > 1
    
def test_returns_array_of_property_instances_from_os():
    array_of_buildings = os_dummy_data["features"]
    props = get_props_from_os(array_of_buildings)
    assert type(props) is list
    assert type(props[0]) is Property

def test_properties_have_desired_attributes():
    array_of_buildings = os_dummy_data["features"]
    props = get_props_from_os(array_of_buildings)
    assert props[0].connectivity == "Semi-Connected"
    assert props[0].age == "1945-1959"
    assert props[0].material == "Brick Or Block Or Stone"
    assert props[0].uprn == 100061342030
    assert props[1].uprn == 100061342031
    assert props[2].connectivity == "Multi-Connected"
    assert props[2].uprn == 10033322698
    assert props[2].age == 2012
    assert props[2].material == "Brick Or Block Or Stone"








    