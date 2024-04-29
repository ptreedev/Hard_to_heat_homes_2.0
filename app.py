from flask import Flask, render_template
from tests.test_multiple_properties import get_props
from src.epc_api import epc_api_call
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    TOKEN = os.getenv("EPC_ENCODED_API_TOKEN")
    # QUERY_PARAMS = {"uprn" : "200002791"}
    QUERY_PARAMS = {"local-authority": "E09000008", "size": "2"}
    HEADERS = {"Accept": "application/json", "Authorization": f"Basic {TOKEN}"}
    array_of_properties = epc_api_call(
        HEADERS, {"local-authority": "E09000008", "size": "50"}
    )["rows"]
    props = get_props(array_of_properties)
    return render_template("home.html", props=props)


# Define other routes as needed

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
