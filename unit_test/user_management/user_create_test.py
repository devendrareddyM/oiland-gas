import json
from unit_test.user_management.user_management_input import *


def test_user_add_OK(client):
    # Issue a GET request.
    response = client.post('/user/add',
                                data=json.dumps(add_user),
                                content_type='application/json')
    return response