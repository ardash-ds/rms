from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import SignInResponseSerializer


def get_tokens_for_user(user):
    """Generates and returns an HTTP response that includes the access and refresh tokens for the given user.

    Arguments:
    - user: A UserModel object representing the user to generate tokens for.
    
    Retern:
      — Response object with access and refresh tokens in json format.
    """
    
    refresh = RefreshToken.for_user(user)
    data = {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }
    serializator = SignInResponseSerializer(data=data)
    serializator.is_valid(raise_exception=True)
    serializator.validated_data
    return Response(
        data=serializator.validated_data, 
        status=200, 
        content_type="application/json",
    )
    
    
def get_token_http_reponse(user, refresh_token: str = None) -> HttpResponse:
    """Generates and returns an HTTP response that includes the access and refresh tokens for the given user.

    Arguments:
    - user: A UserModel object representing the user to generate tokens for.
    - refresh_token: user's 'refresh' token. If provided, generates a new 'access' token for user.

    Return:
    - An HttpResponse object with cookies set for access and refresh tokens.
    """

    http_response = HttpResponse(status=200)
    if refresh_token:
        token = RefreshToken(token=refresh_token)
    else:
        token = RefreshToken.for_user(user)
        http_response.set_cookie("refresh", str(token), httponly=True)
    http_response.set_cookie("access", str(token.access_token), httponly=True)
    return http_response