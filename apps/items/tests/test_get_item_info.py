from typing import List

from django.test import TestCase
from django.urls import reverse

from core.services import TestClientLoginService


class GetItemInfoTestCase(TestCase):
    fixtures = [
        "population/fixtures/test_data.json",
    ]
    
    def setUp(self):
        self.auth_user = TestClientLoginService().auth()
        self.unauth_user = TestClientLoginService().unauth()
        self.valid_url = reverse("get_item_info",  kwargs={"item_id": 1})
        self.invalid_url = reverse("get_item_info",  kwargs={"item_id": 1000})        
        
    def test_get_item_unauthenticated(self):
        response = self.unauth_user.get(path=self.valid_url)
        self.assertEqual(response.status_code, 401) 
           
    def test_get_item_valid_data(self):
        response = self.auth_user.get(path=self.valid_url)
        self.assertEqual(response.status_code, 200) 
        
    def test_get_item_invalid_data(self):
        response = self.auth_user.get(path=self.invalid_url)
        self.assertEqual(response.status_code, 404)
