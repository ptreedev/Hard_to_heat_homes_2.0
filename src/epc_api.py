from src.variables import EPC_BASE_URL
import requests

def epc_api_call(headers, params):

    full_url = f'{EPC_BASE_URL}{params}'

    try:
        response = requests.get(full_url, headers=headers)
        data = response.json()
        return data
    except Exception:
        return False