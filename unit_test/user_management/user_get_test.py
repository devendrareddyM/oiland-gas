def test_user_get_OK(client):
    # Issue a GET request.
    response = client.get('/user/get')
    # Check that the response is OK.
    return response