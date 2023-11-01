from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserModel(AbstractUser):
    email = models.EmailField(
        max_length=50,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # objects = UserManager

    def __str__(self):
        return self.email
