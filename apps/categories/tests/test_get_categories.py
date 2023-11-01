from typing import List

from django.test import Client
from django.urls import reverse_lazy

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import UserModel
from core.services import TestClientLoginService


class GetCategoriesTestCase(TestCase):
    fixtures = [
        "population/fixtures/test_data.json",
    ]
    
    def setUp(self):
        self.auth_user = APIClient()
        self.unauth_user = APIClient()
        self.url = reverse('get_categories')
        user = UserModel.objects.get(email='user1@example.com')
        refresh = RefreshToken.for_user(user)
        self.auth_user.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        
    def test_get_categories_unauthenticated(self):
        response = self.unauth_user.get(path=self.url)
        self.assertEqual(response.status_code, 401) 
           
    def test_get_categories_authenticated(self):
        response = self.auth_user.get(path=self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, List)    
 
        