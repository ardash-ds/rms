from django.contrib.auth import (
    models as auth_models,
    validators,
)
from django.db import models


class UserModel(auth_models.AbstractUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        max_length=50,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = auth_models.UserManager()

    def __str__(self):
        return self.email
