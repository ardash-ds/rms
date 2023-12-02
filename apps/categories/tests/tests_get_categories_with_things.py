import json

from django.test import TestCase
from django.urls import reverse

from core.services import TestClientLoginService


class GetCategoriesWithThingsTestCase(TestCase):
    fixtures = [
        "population/fixtures/test_data.json",
    ]
    
    def setUp(self):
        self.auth_user = TestClientLoginService().auth()
        self.unauth_user = TestClientLoginService().unauth()
        self.url = reverse('get_categories_with_things')
        
    def test_get_categories_with_things_unauthenticated(self):
        response_error = self.unauth_user.get(path=self.url)
        expected_error = {
            "detail": "Authentication credentials were not provided.",
        }
        response_content = json.loads(response_error.content.decode("utf-8"))
        self.assertEqual(response_error.status_code, 401) 
        self.assertEqual(response_content, expected_error) 

           
    def test_get_categories_with_things_authenticated(self):
        response = self.auth_user.get(path=self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)    
    