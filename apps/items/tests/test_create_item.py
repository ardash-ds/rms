# import json

# from django.test import TestCase
# from django.urls import reverse

# from core.services import TestClientLoginService


# class CreateItemTestCase(TestCase):
#     fixtures = [
#         "population/fixtures/test_data.json",
#     ]
    
#     def setUp(self):
#         self.auth_user = TestClientLoginService().auth('user1@example.com')
#         self.unauth_user = TestClientLoginService().unauth()
#         self.url = reverse("create_item")
#         # self.full_data = {'item': ['{  "name": "str11ing",  "description": "string",  "category": 1,  "storage": 1}'], 'image_list': ['']}
#         self.full_data = {
#             "item": 
#                 {
#                     "name": "string",
#                     "description": "string",
#                     "category": 1,
#                     "storage": 1
#                 }
#             ,
#             "image_list": [''],
#         }
#         self.optional_data = {
#             "name": "string",
#             "description": "",
#             "category": 1,
#             "storage": 1
#         }
#         self.empty_required_data = {
#             "name": "",
#             "description": "string",
#             "category": 1,
#             "storage": 1
#         }
#         self.invalid_category_data = {
#             "name": "string",
#             "description": "string",
#             "category": 1000,
#             "storage": 1
#         }
#         self.invalid_storage_data = {
#             "name": "string",
#             "description": "string",
#             "category": 1,
#             "storage": 6
#         }
      
        
#     def test_create_item_unauthenticated(self):
#         response_error = self.unauth_user.post(path=self.url)
#         expected_error = {
#             "detail": "Authentication credentials were not provided.",
#         }
#         response_content = json.loads(response_error.content.decode("utf-8"))
#         self.assertEqual(response_error.status_code, 401) 
#         self.assertEqual(response_content, expected_error) 
           
#     def test_create_item_full_data(self):
#         response = self.auth_user.post(
#             path=self.url, 
#             data=self.full_data,
#             content_type="multipart/form-data",
#         )
#         response_content = json.loads(response.content.decode("utf-8"))
#         self.assertEqual(response.status_code, 201) 
#         self.assertEqual(response_content['name'], self.full_data['name']) 
#         self.assertEqual(response_content['description'], self.full_data['description'])
#         self.assertEqual(response_content['category']['id'], self.full_data['category']) 
#         self.assertEqual(response_content['storage']['id'], self.full_data['storage']) 

#     # def test_get_item_invalid_data(self):
#     #     response_error = self.auth_user.get(path=self.invalid_url)
#     #     expected_error = {
#     #         "detail": "Not found.",
#     #     }
#     #     response_content = json.loads(response_error.content.decode("utf-8"))
#     #     self.assertEqual(response_error.status_code, 404)
#     #     self.assertEqual(response_content, expected_error)