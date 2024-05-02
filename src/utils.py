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
            age = "buildingage_year" if building["buildingage_year"] else "buildingage_period"
            new_prop = Property(uprn_array[j]['uprn'])
            new_prop.connectivity =  building["connectivity"]
            new_prop.age =  building[age]
            new_prop.material =  building["constructionmaterial"]
            epc_result = epc_api_call({"Accept": "application/json", "Authorization": f'Basic {TOKEN}'}, {"uprn": uprn_array[j]["uprn"]})
            new_prop.epc_rating = epc_result["rows"][0]["current-energy-rating"] if epc_result else 'Not found'
            new_prop.epc_score = epc_result["rows"][0]["current-energy-efficiency"] if epc_result else 'Not found'
            new_prop.address = f'{epc_result["rows"][0]["address"]}, {epc_result["rows"][0]["postcode"]}' if epc_result else 'Not found'
            result.append(new_prop)

    return result