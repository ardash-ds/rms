import json

from django.test import Client
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import UserModel


class TestClientLoginService:
    """A class that provides different user roles for testing client login functionality.

    Methods:
        unauth(): Returns an unauthenticated client.
        auth(): Returns an authenticated client.
    """
    
    def __init__(self):
        """Initializes the TestClientLoginService with a Django test 
        client and the paths for sign in and sign up.
        """
        
        self.client = APIClient()
        self.sign_in_path = reverse("sign_in")

    def unauth(self):
        """
        Returns:
            Client: The unauthenticated Django test client.
        """
        
        return APIClient()
    
    def auth(self):
        """
        Returns:
            Client: The authenticated Django test client.
        """
        
        data = {
            "email": "user1@example.com",
            "password": "qwerty1234"
        }
        # self.client.post(path=self.sign_in_path, data=data, content_type="application/json")
        # print(self.client.head)
        # user = UserModel.objects.get(email='user1@example.com')
        # refresh = RefreshToken.for_user(user)
        # self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh}')
        return self.client

def test_client_login():
    client = APIClient()
    path = reverse("sign_in")
    user = UserModel.objects.get(email='user1@example.com')
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh}')
    response = client.get(path=reverse('get_storage_all'))
    return client
    