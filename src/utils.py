from src.property import Property
import os
from dotenv import load_dotenv
from src.epc_api import epc_api_call

load_dotenv()
TOKEN = os.getenv("EPC_ENCODED_API_TOKEN")


def get_props_from_os(list_of_buildings):
    result = []
    for i in range(len(list_of_buildings)):
        building = list_of_buildings[i]["properties"]
        uprn_array = building["uprnreference"]
        for j in range(len(uprn_array)):
            age = (
                "buildingage_year"
                if building["buildingage_year"]
                else "buildingage_period"
            )
            new_prop = Property(uprn_array[j]["uprn"])
            new_prop.connectivity = building["connectivity"]
            new_prop.age = building[age]
            new_prop.material = building["constructionmaterial"]
            result.append(new_prop)

    return result


def get_attributes_from_epc(properties):
    epc_params = get_urpns_from_properties(properties)
    epc_result_rows = epc_api_call(
        {"Accept": "application/json", "Authorization": f"Basic {TOKEN}"}, epc_params
    )["rows"]
    for i in range(len(properties)):
        prop = properties[i]
        for j in range(len(epc_result_rows)):
            if str(prop.uprn) == epc_result_rows[j]["uprn"]:
                prop.epc_rating = epc_result_rows[j]["current-energy-rating"]
                prop.epc_score = epc_result_rows[j]["current-energy-efficiency"]
                prop.address = (
                    f'{epc_result_rows[j]["address"]}, {epc_result_rows[j]["postcode"]}'
                )
                

def get_urpns_from_properties(properties):
    base_str = "uprn"
    result = ""
    for prop in properties:
        result += f"{base_str}={prop.uprn}&"
    return result
