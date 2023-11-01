from typing import List

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import UserModel


class GetItemInfoTestCase(TestCase):
    
    fixtures = [
        "population/fixtures/test_data.json",
    ]
    
    def setUp(self):

        self.auth_user = APIClient()
        self.unauth_user = APIClient()
        self.valid_url = reverse("get_item_info",  kwargs={"item_id": 1})
        self.invalid_url = reverse("get_item_info",  kwargs={"item_id": 1000})        
        user = UserModel.objects.get(email='user1@example.com')
        refresh = RefreshToken.for_user(user)
        self.auth_user.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_get_item_unauthenticated(self):
        response = self.unauth_user.get(path=self.valid_url)
        self.assertEqual(response.status_code, 401) 
           
    def test_get_item_valid_data(self):
        response = self.auth_user.get(path=self.valid_url)
        self.assertEqual(response.status_code, 200) 
        
    def test_get_item_invalid_data(self):
        response = self.auth_user.get(path=self.invalid_url)
        self.assertEqual(response.status_code, 404)
