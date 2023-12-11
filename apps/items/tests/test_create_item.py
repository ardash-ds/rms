import json

from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from core.services import TestClientLoginService


class CreateItemTestCase(TestCase):
    fixtures = [
        "population/fixtures/test_data.json",
    ]
    
    def setUp(self):
        self.auth_user = TestClientLoginService().auth('user1@example.com')
        self.unauth_user = TestClientLoginService().unauth()
        self.url = reverse("create_item")
        image_content = (
            b"\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF\xDB\x00\x43\x00\x06\x04\x05\x06\x05\x04"
        )       
        self.file = SimpleUploadedFile(
            "foto1.jpg", 
            image_content, 
            content_type="image/jpeg"
        )
        self.full_data = {
            "name": "string",
            "description": "string",
            "category": 1,
            "storage": 1
        }
        self.optional_data = {
            "name": "string",
            "description": "",
            "category": 1,
            "storage": 1
        }
        self.empty_required_data = {
            "name": "",
            "description": "string",
            "category": 1,
            "storage": 1
        }
        self.invalid_category_data = {
            "name": "string",
            "description": "string",
            "category": 1000,
            "storage": 1
        }
        self.invalid_storage_data = {
            "name": "string",
            "description": "string",
            "category": 1,
            "storage": 1000
        }
      
        
    def test_create_item_unauthenticated(self):
        response_error = self.unauth_user.post(path=self.url)
        expected_error = {
            "detail": "Authentication credentials were not provided.",
        }
        response_content = json.loads(response_error.content.decode("utf-8"))
        self.assertEqual(response_error.status_code, 401) 
        self.assertEqual(response_content, expected_error) 
           
    def test_create_item_full_data(self):
        response = self.auth_user.post(
            path=self.url, 
            data={
            "item": json.dumps(self.full_data),
            "image_list": [self.file,],
        },
            content_type=None,
        )
        response_content = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 201) 
        self.assertEqual(response_content['name'], self.full_data['name']) 
        self.assertEqual(response_content['description'], self.full_data['description'])
        self.assertEqual(response_content['category']['id'], self.full_data['category']) 
        self.assertEqual(response_content['storage']['id'], self.full_data['storage']) 
        self.assertEqual(response_content['storage']['id'], self.full_data['storage']) 
        
    def test_create_item_optional_data(self):
        response = self.auth_user.post(
            path=self.url, 
            data={
            "item": json.dumps(self.optional_data),
            "image_list": [],
        },
            content_type=None,
        )
        response_content = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 201) 
        self.assertEqual(response_content['name'], self.optional_data['name']) 
        self.assertEqual(response_content['description'], self.optional_data['description'])
        self.assertEqual(response_content['category']['id'], self.optional_data['category']) 
        self.assertEqual(response_content['storage']['id'], self.optional_data['storage']) 
        self.assertEqual(response_content['storage']['id'], self.optional_data['storage']) 
        
    def test_create_item_empty_required_data(self):
        response = self.auth_user.post(
            path=self.url, 
            data={
            "item": json.dumps(self.empty_required_data),
            "image_list": [],
        },
            content_type=None,
        )
        response_content = json.loads(response.content.decode("utf-8"))
        expected_error = {'name': ['This field may not be blank.']}
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_content, expected_error)
        
    def test_create_item_invalid_category_data(self):
        response = self.auth_user.post(
            path=self.url, 
            data={
            "item": json.dumps(self.invalid_category_data),
            "image_list": [],
        },
            content_type=None,
        )
        response_content = json.loads(response.content.decode("utf-8"))
        expected_error = {'category': ['Invalid pk "1000" - object does not exist.']}
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_content, expected_error)
        
    def test_create_item_invalid_storage_data(self):
        response = self.auth_user.post(
            path=self.url, 
            data={
            "item": json.dumps(self.invalid_storage_data),
            "image_list": [],
        },
            content_type=None,
        )
        response_content = json.loads(response.content.decode("utf-8"))
        expected_error = {'storage': ['Invalid pk "1000" - object does not exist.']}
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_content, expected_error)
        