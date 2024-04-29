# Getting started 

How to set up the python virtual environment
```shell
python3 -m venv .
source bin/activate
pip install -r requirements.txt
```
### Setting up the .env
The .env file requires the following:
EPC_ENCODED_API_TOKEN

#### How to get your EPC_ENCODED_API_TOKEN

- You need to set an account with EPC open data communities [sign up/in](https://epc.opendatacommunities.org/login)
- Make an API call using postman for example 
    - end point: https://epc.opendatacommunities.org/api/v1/domestic/search
    - Authorisation type: Basic auth
    - Username: your email you signed up with
    - Password: Your API key from EPC open data account
- You should be able to find your EPC_ENCODED_API_TOKEN in your 'authorization'

# To run app

```shell
flask run
```