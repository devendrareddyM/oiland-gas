import json
from unit_test.user_management.user_management_input import *


def test_user_update_OK(client):
    # Issue a GET request.
    response = client.put('/user/modify',
                          data=json.dumps(modify_user),
                          content_type='application/json')
    # Check that the response is OK.
    return response
