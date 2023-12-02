import json

from django.test import TestCase
from django.urls import reverse

from core.services import TestClientLoginService


class GetItemInfoTestCase(TestCase):
    fixtures = [
        "population/fixtures/test_data.json",
    ]
    
    def setUp(self):
        self.auth_user = TestClientLoginService().auth('user1@example.com')
        self.unauth_user = TestClientLoginService().unauth()
        self.valid_url = reverse("get_item_info",  kwargs={"item_id": 1})
        self.invalid_url = reverse("get_item_info",  kwargs={"item_id": 1000})        
        
    def test_get_item_unauthenticated(self):
        response_error = self.unauth_user.get(path=self.valid_url)
        expected_error = {
            "detail": "Authentication credentials were not provided.",
        }
        response_content = json.loads(response_error.content.decode("utf-8"))
        self.assertEqual(response_error.status_code, 401) 
        self.assertEqual(response_content, expected_error) 
           
    def test_get_item_valid_data(self):
        response = self.auth_user.get(path=self.valid_url)
        self.assertEqual(response.status_code, 200) 
        
    def test_get_item_invalid_data(self):
        response_error = self.auth_user.get(path=self.invalid_url)
        expected_error = {
            "detail": "Not found.",
        }
        response_content = json.loads(response_error.content.decode("utf-8"))
        self.assertEqual(response_error.status_code, 404)
        self.assertEqual(response_content, expected_error)
