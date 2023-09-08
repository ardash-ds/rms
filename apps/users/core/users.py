import requests

from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from rest_framework import exceptions
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.forms import ValidationError
from django.http import HttpRequest

from ..serializers import (
    UserRegistrationRequestSerializer, 
    UserRefreshSerializer,
)
from ..models import UserModel


# =============================================POST=============================================

@transaction.atomic
def sign_up_core(request: HttpRequest) -> None:
    """Signs up a user, given their email and password.

    Args:
        request (django.http.HttpRequest): The HTTP request object.

    Returns:
        None
    """
    data = JSONParser().parse(request)
    serializer = UserRegistrationRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    email = serializer.validated_data["email"]
    password = serializer.validated_data["password"]

    UserModel.objects.create_user(username=email, email=email, password=password)

    
@transaction.atomic
def sign_in_core(request: HttpRequest) -> UserModel:
    """
    Sign in a user, given their email and password.

    Args:
        request (django.http.HttpRequest): The HTTP request object.

    Returns:
        UserModel: Present in database user object.
    """

    data = JSONParser().parse(request)
    email = data['email']
    password = data['password']
    try:
        user = UserModel.objects.get(email=email)
        if not user.check_password(password):
            raise AuthenticationFailed()
    except UserModel.DoesNotExist:
        raise AuthenticationFailed()
    return user


def refresh_token_validation_core(request: HttpRequest) -> str:
    data = {"refresh": request.COOKIES.get('refresh')}
    serialized_data = UserRefreshSerializer(data=data)
    serialized_data.is_valid(raise_exception=True)
    return serialized_data
    