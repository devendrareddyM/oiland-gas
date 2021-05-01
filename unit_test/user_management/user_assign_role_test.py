import json
from unit_test.user_management.user_management_input import *


def test_user_role(client):
    response = client.put('/user/role',
                           data=json.dumps(assign_role),
                           content_type='application/json')
    return response
