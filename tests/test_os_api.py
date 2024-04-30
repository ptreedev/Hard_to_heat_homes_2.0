def os_api_call(headers):
    return False

def test_not_200_response():
    assert os_api_call({}) == False