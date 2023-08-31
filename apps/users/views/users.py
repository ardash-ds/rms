from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)

from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import AllowAny

from django.http import HttpResponse, HttpRequest

from ..core import sign_in_core, sign_up_core
from ..serializers import (
    UserRegistrationRequestSerializer,
)
from ..services import get_tokens_for_user


# =============================================POST=============================================


@extend_schema(
    summary="WORKS: Sign-up by email and password",
    description="Take email and password, create user and return 'access' and 'refresh' tokens in cookies",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
    responses={
        201: OpenApiResponse(description="Successfully registrated."),
        400: OpenApiResponse(description="Error: Bad request"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "users",
    ],
)
@api_view(["POST"])
def sign_up(request: HttpRequest) -> HttpResponse:
    sign_up_core(request=request)
    return HttpResponse(status=201)

@extend_schema(
    description="WORKS: Take user's email and password and return 'access' and 'refresh' tokens in cookies",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
    responses={
        200: OpenApiResponse(description="Successfully registrated."),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(['POST'])
def sign_in(request: HttpRequest) -> HttpResponse:
    user = sign_in_core(request=request)
    return get_tokens_for_user(user)

