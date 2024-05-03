import json
import urllib.request
from urllib.parse import urlencode
from src.variables import OS_BASE_URL

def os_api_call(headers, params):
    full_url = f"{OS_BASE_URL}{urlencode(params)}"
    try:
        with urllib.request.urlopen(
            urllib.request.Request(full_url, headers=headers)
        ) as response:
            response_body = response.read()
            return json.loads(response_body)

    except Exception:
        return False