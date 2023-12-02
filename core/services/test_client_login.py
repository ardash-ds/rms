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
    
    def auth(self, email: str = 'user1@example.com'):
        """
        Returns:
            Client: The authenticated Django test client.
        """

        user = UserModel.objects.get(email=email)
        print(user)
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        return self.client
    