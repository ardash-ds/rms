from typing import List

from django.test import TestCase
from django.urls import reverse

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

from apps.users.models import UserModel


class GetItemsTestCase(TestCase):
    fixtures = [
        "population/fixtures/test_data.json"
    ]
        
    def setUp(self):
        self.auth_user = APIClient()
        self.unauth_user = APIClient()
        
        user = UserModel.objects.get(email='user1@example.com')
        refresh = RefreshToken.for_user(user)
        self.auth_user.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.url = reverse('get_items')
        
    def test_get_items_unauthenticated(self):
        response = self.unauth_user.get(path=self.url)
        self.assertEqual(response.status_code, 401) 
           
    def test_get_items_authenticated(self):
        response = self.auth_user.get(path=self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, List)    
 
        