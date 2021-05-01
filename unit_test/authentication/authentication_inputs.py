valid_payload = {
    "username": "admin",
    "password": "password"
}
invalid_payload = {
    "username": "admin111",
    "password": "password111"
}

success_payload_response = {
    "token": "text"
}

failure_payload_response = {
    "message": "unauthorised"
}

token = {
    'token': "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
             ".eyJ1c2VyX2lkIjoxLCJmaXJzdF9uYW1lIjoiU "
             "3VzaGFudCIsInJvbGVfaWQiOjF9.7"
             "-YM8xa2DFv8nBjYzBl1jUbHAjhIKeoww3s8Njp1iAA'"}
