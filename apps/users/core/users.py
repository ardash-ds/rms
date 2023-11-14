import json

from rest_framework.parsers import JSONParser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from django.db import transaction
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404

from ..serializers import (
    UserInfoResponseSerializer,
    UserRegistrationRequestSerializer, 
    UserRefreshRequestSerializer,
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
    first_name = serializer.validated_data["first_name"]

    UserModel.objects.create_user(
        username=email, 
        email=email, 
        password=password, 
        first_name=first_name
    )

    
@transaction.atomic
def sign_in_core(request: HttpRequest) -> UserModel:
    """
    Sign in a user, given their email and password.

    Args:
    - request (HttpRequest): A Django HttpRequest object, containing user 
      authentication and authorization.

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


def blacklists_the_token(request: HttpRequest) -> str:
    """
    Receives a refresh token and blacklists it.

    Args:
    - request (HttpRequest): A Django HttpRequest object, containing refresh token.

    Returns:
        HttpResponse object with status code.
    """
    
    data = JSONParser().parse(request)
    serialized_data = UserRefreshRequestSerializer(data=data)
    serialized_data.is_valid(raise_exception=True)
    try:
        token = RefreshToken(serialized_data.data.get('refresh'))
        token.blacklist()
        return HttpResponse(status=204)
    except Exception as e:
        return HttpResponse(status=422, content=e)
    


# =============================================GET=============================================


def get_user_info_core(request: HttpRequest):
    """
    Get user data.

    Args:
    - request (HttpRequest): A Django HttpRequest object, containing user 
      authentication and authorization.

    Returns:
        UserModel: Present in database user object.
    """
    return UserInfoResponseSerializer(
        get_object_or_404(UserModel, id=request.user.id)
    )
    