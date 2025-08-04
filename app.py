from flask import Flask, render_template
from src.os_api import os_api_call
from src.utils import get_properties_from_os, get_attributes_from_epc, set_missing_addresses, setting_void_properties
from src.variables import OS_KEY

app = Flask(__name__)

HEADERS = {"Accept": "application/json"}
PARAMS = {
        "key": OS_KEY,
        "filter": "buildinguse_oslandusetiera = 'Residential Accommodation' AND mainbuildingid_ismainbuilding = 'Yes'",
        "bbox": "-0.373641,51.399234,-0.372031,51.399977",
         }
list_of_buildings = os_api_call(HEADERS, PARAMS)["features"]

properties = get_properties_from_os(list_of_buildings)

setting_void_properties(properties)
for i in range(len(properties)):
    # set_missing_addresses(properties[i])
    properties[i].calculate_score()


@app.route("/")
def home():
   return render_template("home.html", properties=properties, key=OS_KEY)

@app.route("/<int:uprn>")
def property(uprn):
    
    prop = None
    for property in properties:
        if property.uprn == uprn:
            prop = property 
            break
    get_attributes_from_epc(prop, uprn)
        
    return render_template("property.html", property=prop, key=OS_KEY)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
