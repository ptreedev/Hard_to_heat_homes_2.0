from src.council_data_utils import filter_properties_by_council_code
from src.utils import get_properties_from_os
import json
from src.property import Property

with open("tests/test_data/os_dummy_data.json") as data:
    os_dummy_data = json.load(data)
    
array_of_buildings = os_dummy_data["features"]
props = get_properties_from_os(array_of_buildings)
dummy_uprn = 10090058306
dummy_prop = Property(dummy_uprn)

props.append(dummy_prop)

def test_filter_properties_in_elmbridge():
    elmbridge_council_code = "E07000207"
    filtered_props = filter_properties_by_council_code(elmbridge_council_code, props)

    assert filtered_props == props[:4]

def test_filter_properties_in_east_hampshire():
    east_hampshire_council_code = "E07000085"
    filtered_props = filter_properties_by_council_code(east_hampshire_council_code, props)

    assert filtered_props == []

def test_filter_properties_in_tunbridge_wells():
    tunbridge_wells_council_code = "E07000116"
    filtered_props = filter_properties_by_council_code(tunbridge_wells_council_code, props)

    assert filtered_props == [dummy_prop]

def test_filter_properties_in_None():
    filtered_props = filter_properties_by_council_code(None, props)

    assert filtered_props == []    
