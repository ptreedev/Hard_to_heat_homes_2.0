import json
import urllib.request
from urllib.parse import urlencode

BASE_URL = 'https://epc.opendatacommunities.org/api/v1/domestic/search?'

def epc_api_call(headers, params):

    encoded_params = urlencode(params)
    full_url = f'{BASE_URL}{encoded_params}'

    try:
        with urllib.request.urlopen(urllib.request.Request(full_url, headers=headers)) as response:
            response_body = response.read()

            if len(response_body) > 0:
                return json.loads(response_body)
            else: return {}
    except Exception:
        return False