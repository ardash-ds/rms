from django.contrib.auth import (
    models as auth_models,
    validators,
)
from django.db import models


class UserModel(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username_validator = validators.UnicodeUsernameValidator()
    username = models.CharField(
        "username",
        max_length=30,
        unique=True,
        help_text="Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    description = models.TextField(max_length=100, null=True)
    email = models.EmailField(
        max_length=50,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
