from flask import Flask, render_template
from src.epc_api import epc_api_call
import os
from dotenv import load_dotenv
from src.property import Property

load_dotenv()

app = Flask(__name__)

def get_props(props):
    result = []
    for prop in props:
        result.append(
            Property(
                prop["uprn"],
                prop["current-energy-rating"],
                prop["current-energy-efficiency"],
                prop["address"],
                prop["postcode"],
            )
        )

    return result


@app.route("/")
def home():
    TOKEN = os.getenv("EPC_ENCODED_API_TOKEN")
    QUERY_PARAMS = {"local-authority": "E09000008", "size": "5"}
    HEADERS = {"Accept": "application/json", "Authorization": f"Basic {TOKEN}"}
    array_of_properties = epc_api_call(HEADERS, QUERY_PARAMS)["rows"]
    props = get_props(array_of_properties)
    return render_template("home.html", props=props)


# Define other routes as needed

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
