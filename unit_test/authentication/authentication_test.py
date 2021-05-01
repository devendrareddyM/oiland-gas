import json
from unit_test.authentication.authentication_inputs import *


def test_login_failed(client):
    # Issue a POST request.
    response = client.post('/auth', data=json.dumps(invalid_payload),
                           content_type='application/json')
    return response, failure_payload_response


def test_login_passed(client):
    # Issue a POST request.
    response = client.post('/auth', data=json.dumps(valid_payload)
                           , content_type='application/json')
    return response, token
