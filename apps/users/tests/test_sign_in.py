import json

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient


class SignInTestCase(TestCase):
    fixtures = [
        "population/fixtures/test_data.json",
    ]
    
    def setUp(self):
        self.valid_data = {
            "email": "user1@example.com",
            "password": "qwerty1234"
        }
        self.invalid_data = {
            "email": "user2@example.com",
            "password": "sdadadadasdad"
        }
        self.url = reverse("sign_in")
        self.client = APIClient()
        
    def test_sign_in_valid_data(self):
        response = self.client.post(
            path=self.url,
            data=json.dumps(self.valid_data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200) 
           
    def test_sign_in_invalid_data(self):
        response = self.client.post(
            path=self.url,
            data=json.dumps(self.invalid_data),
            content_type="application/json",
        )
        self.assertEqual(response.content, b'{"detail":"Incorrect authentication credentials."}')
        self.assertEqual(response.status_code, 401)  
 