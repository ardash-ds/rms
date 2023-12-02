from typing import List

from django.test import Client
from django.urls import reverse_lazy

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from core.services import TestClientLoginService


class GetStorageUserTestCase(TestCase):
    fixtures = [
        "population/fixtures/test_data.json",
    ]
    def setUp(self):
        self.auth_user = TestClientLoginService().auth('user1@example.com')
        self.unauth_user = TestClientLoginService().unauth()
        self.url = reverse('get_storage_all')
        
    def test_get_storage_unauthenticated(self):
        response = self.unauth_user.get(path=self.url)
        self.assertEqual(response.status_code, 401) 
           
    def test_get_storage_authenticated(self):
        response = self.auth_user.get(path=self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, List)    
