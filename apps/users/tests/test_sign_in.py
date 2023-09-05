import json

from django.test import TestCase
from django.urls import reverse

from core.services import TestClientLoginService


class SignInTestCase(TestCase):
    def setUp(self):
        self.url = reverse("sign_in")
        self.unauth_user = TestClientLoginService().unauth()
        
        self.valid_data = {
            "email": "user2@example.com",
            "password": "qwerty1234"
        }
        
        self.invalid_data = {
            "email": "user2@example.com",
            "password": "sdadadadasdad"
        }
        
    def test_sign_in_valid_data(self):
        response = self.unauth_user.post(
            path=self.url,
            data=json.dumps(self.valid_data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200) 
           
    def test_sign_in_invalid_data(self):
        response = self.unauth_user.post(
            path=self.url,
            data=json.dumps(self.invalid_data),
            content_type="application/json",
        )
        self.assertEqual(response.content, b'{"detail":"Incorrect authentication credentials."}')
        self.assertEqual(response.status_code, 401)  
 