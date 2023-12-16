import json

from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from core.services import TestClientLoginService


class DeleteItemTestCase(TestCase):
    fixtures = [
        "population/fixtures/test_data.json",
    ]
    
    def setUp(self):
        self.item_id = 1
        self.auth_user = TestClientLoginService().auth('user1@example.com')
        self.unauth_user = TestClientLoginService().unauth()
        self.valid_url = reverse("delete_item",  kwargs={"item_id": self.item_id})
        self.invalid_url = reverse("delete_item",  kwargs={"item_id": 1000})
        
    def test_delete_item_unauthenticated(self):
        response_error = self.unauth_user.delete(path=self.valid_url)
        expected_result = {
            "detail": "Authentication credentials were not provided.",
        }
        response_content = json.loads(response_error.content.decode("utf-8"))
        self.assertEqual(response_error.status_code, 401) 
        self.assertEqual(response_content, expected_result) 

    def test_delete_item_authenticated_valid_url(self):
        response = self.auth_user.delete(path=self.valid_url)
        expected_result = {
            "detail": f"Item (id:{self.item_id}) was successfully deleted"
        }
        response_content = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response_content, expected_result) 
        
    def test_delete_item_authenticated_invalid_url(self):
        response = self.auth_user.delete(path=self.invalid_url)
        expected_result = {
            "detail": "Not found."
        }
        response_content = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 404) 
        self.assertEqual(response_content, expected_result) 
        