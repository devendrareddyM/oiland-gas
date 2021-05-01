def test_user_availbility_OK(client):
    # Issue a GET request.
    response = client.get('/user/availbility?user_name=admin')
    # Check that the response is OK.
    return response


def test_user_availbility_FAIL(client):
    # Issue a GET request.
    response = client.get('/user/availbility')
    # Check that the response is OK.
    return response