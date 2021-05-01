import unittest

from django.test import Client

from unit_test.authentication.authentication_test import *
from unit_test.user_management.user_assign_role_test import *
from unit_test.user_management.user_availabilty_test import *
from unit_test.user_management.user_create_test import *
from unit_test.user_management.user_get_test import *
from unit_test.user_management.user_getall_test import *
from unit_test.user_management.user_modify_test import *
from supports.status import HTTP_200_OK, \
    HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

tc = unittest.TestCase


class SimpleTest(tc):

    def successful_response(self, response):
        # Check that the response is OK.
        self.assertEqual(response.status_code, HTTP_200_OK)
        # Check if content data is available
        self.assertIsNotNone(response.content)

    def unauthorized(self, response):
        # Check that the response is unauthorized.
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)
        # Check if content data is available
        self.assertIsNotNone(response.content)

    def content_verification(self, response, payload_response):
        data = response.content
        json_payload = json.loads(data.decode('utf-8'))
        # Check if content value ~ expected value
        self.assertAlmostEquals(json_payload, payload_response)
        # Check if keys are correct
        self.assertEqual(json_payload.keys(), payload_response.keys())

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' \
                                                     'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.' \
                                                     'eyJ1c2VyX2lkIjoxLCJmaXJzdF9uYW1lIjoi' \
                                                     'RGljayIsInJvbGVfaWQiOjF9.8LXEYNg1QRW' \
                                                     'QZJSQjJdV44AIFljYQx3IOi_bh722LVw'
        self.token = {
            "token": "b'eyJ0eXAiOiJKV1Qi"
                     "LCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ"
                     "maXJzdF9uYW1lIjoiRGljayIsInJvbGVfaWQiOjF9"
                     ".8LXEYNg1QRWQZJSQjJdV44AIFljYQx3IOi_bh722LVw'"
        }

    def test_login_passed(self):
        response, success_payload = test_login_passed(
            self.client)
        self.successful_response(response)
        # self.content_verification(response, success_payload)

    def test_login_failed(self):
        response, failure_payload = test_login_failed(self.client)
        self.unauthorized(response)
        # self.content_verification(response, failure_payload)

    # All GET METHODS
    def test_user_get_OK(self):
        response = test_user_get_OK(self.client)
        self.successful_response(response)

    def test_user_getall_OK(self):
        response = test_user_getall_OK(self.client)
        self.successful_response(response)

    def test_user_availbility_OK(self):
        response = test_user_availbility_OK(self.client)
        self.successful_response(response)

    def test_user_availbility_FAIL(self):
        response = test_user_availbility_FAIL(self.client)
        self.successful_response(response)

    def test_user_role(self):
        response = test_user_role(self.client)
        self.successful_response(response)

    # insert and update method
    def test_user_add_OK(self):
        response = test_user_add_OK(self.client)
        self.successful_response(response)

    def test_user_update_OK(self):
        response = test_user_update_OK(self.client)
        self.successful_response(response)

    # def test_y_deleted_OK(self):
    #     # Issue a GET request.
    #     response = self.client \
    #         .post('/delete/test',
    #               data={
    #                   "user_name": add_user["user_name"]
    #               },
    #               content_type='application/json')
    #     # Check that the response is OK.
    #     self.successful_response(response)
