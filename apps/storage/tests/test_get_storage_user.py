from typing import List

from django.test import Client
from django.urls import reverse_lazy

from django.test import TestCase
from django.urls import reverse

from core.services import TestClientLoginService


class GetStorageUserTestCase(TestCase):
    def setUp(self):
        self.url = reverse('get_storage_all')
        self.unauth_user = TestClientLoginService().unauth()
        self.auth_user = TestClientLoginService().auth()
        
    def test_get_storage_unauthenticated(self):
        response = self.unauth_user.get(path=self.url)
        self.assertEqual(response.status_code, 401) 
           
    def test_get_storage_authenticated(self):
        response = self.auth_user.get(path=self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, List)    
