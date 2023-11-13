from typing import List

from django.test import TestCase
from django.urls import reverse

from core.services import TestClientLoginService


class GetItemsTestCase(TestCase):
    fixtures = [
        "population/fixtures/test_data.json"
    ]
        
    def setUp(self):
        self.auth_user = TestClientLoginService().auth()
        self.unauth_user = TestClientLoginService().unauth()
        self.url = reverse('get_items')
        
    def test_get_items_unauthenticated(self):
        response = self.unauth_user.get(path=self.url)
        self.assertEqual(response.status_code, 401) 
           
    def test_get_items_authenticated(self):
        response = self.auth_user.get(path=self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, List)    
 
        