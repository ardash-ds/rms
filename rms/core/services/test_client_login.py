from django.test import Client
from django.urls import reverse_lazy


class TestClientLoginService:
    """A class that provides different user roles for testing client login functionality.

    Methods:
        unauth(): Returns an unauthenticated client.
        auth(): Returns an authenticated client.
    """
    
    def __init__(self):
        """Initializes the TestClientLoginService with a Django test client and the paths for sign in and sign up."""
        self.client = Client()
        self.sign_in_path = reverse_lazy("sign_in")

    def unauth(self):
        """
        Returns:
            Client: The unauthenticated Django test client.
        """
        return Client()
    
    def auth(self):
        """
        Returns:
            Client: The authenticated Django test client.
        """
        data = {
            "email": "admin@admin.ru",
            "password": "1234",
        }
        # data = {
        #     "email": "user1@example.com",
        #     "password": "qwerty1234",
        # }
        self.client.post(
            path=self.sign_in_path, 
            data=data, 
            content_type="application/json"
        )
        return self.client
    