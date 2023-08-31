from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import SignInResponseSerializer


def get_tokens_for_user(user):
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
    