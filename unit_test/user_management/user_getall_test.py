def test_user_getall_OK(client):
    # Issue a GET request.
    response = client.get('/user/getall?lmt=5')
    # Check that the response is OK.
    return response