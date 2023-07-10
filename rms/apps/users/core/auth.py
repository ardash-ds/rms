import requests

from rest_framework.parsers import JSONParser
from rest_framework.utils import json

from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.forms import ValidationError
from django.http import HttpRequest

from ..models import (
    UserModel,
    UserAuthTypeModel,
)

from ..serializers import UserRefreshRequestSerializer

from ..services import UserManagerService

from core.services import GenerateRandomStringService


@transaction.atomic
def sign_up_core(request: HttpRequest) -> UserModel:
    """
    Signs up a user, given their email and password, and generates a random username for them.

    Args:
        request (django.http.HttpRequest): The HTTP request object.

    Returns:
        UserModel: The newly created user object.
    """
    data = JSONParser().parse(request)
    email = data['email']
    password = data['password']
    username = GenerateRandomStringService.get_random_username()
    user = UserModel.objects.create_user(email=email, password=password, username=username)
    return user