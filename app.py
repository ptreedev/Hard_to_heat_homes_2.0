from flask import Flask, render_template
from src.epc_api import epc_api_call
import os
from dotenv import load_dotenv
from src.property import Property
from tests.test_os_api import os_api_call
from src.utils import *
load_dotenv()

app = Flask(__name__)




@app.route("/")
def home():
    TOKEN = os.getenv("EPC_ENCODED_API_TOKEN")
    OS_API_KEY = os.getenv("OS_API_KEY")
    QUERY_PARAMS = {"local-authority": "E09000008", "size": "5"}
    HEADERS = {"Accept": "application/json", "Authorization": f"Basic {TOKEN}"}
    # array_of_properties = epc_api_call(HEADERS, QUERY_PARAMS)["rows"]
    # props = get_props(array_of_properties)
    list_of_buildings = os_api_call({"Accept":"application/json"}, {
        "key": OS_API_KEY,
        "filter": "oslandusetiera LIKE 'Residential Accommodation' AND ismainbuilding=true",
        "bbox": "-0.372438,51.405655,-0.371885,51.40600",
    })["features"]
    props = get_props_from_os(list_of_buildings)
    return render_template("home.html", props=props)


# Define other routes as needed

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
