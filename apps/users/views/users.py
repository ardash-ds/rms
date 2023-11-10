from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)

from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from django.http import HttpResponse, HttpRequest

from ..core import (
    blacklists_the_token,
    get_user_info_core, 
    sign_in_core, 
    sign_up_core,
)
from ..serializers import (
    UserInfoResponseSerializer,
    UserRegistrationRequestSerializer,
    UserRefreshRequestSerializer,
)
from ..services import (
    get_tokens_for_user, 
    get_token_http_response,
)


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
@permission_classes([AllowAny])
def sign_up(request: HttpRequest) -> HttpResponse:
    sign_up_core(request=request)
    return HttpResponse(status=201)


@extend_schema(
    summary="WORKS: Signin",
    description="Take user's email and password and return 'access' and 'refresh' tokens",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
    responses={
        200: OpenApiResponse(description="Successfully registrated."),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "users",
    ],
)
@api_view(['POST'])
@permission_classes([AllowAny])
def sign_in(request: HttpRequest) -> HttpResponse:
    user = sign_in_core(request=request)
    return get_tokens_for_user(user)


@extend_schema(
    description="WORKS: Take user's email and password and return 'access' and 'refresh' tokens in cookies",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
    responses={
        200: OpenApiResponse(description="Successfully registrated."),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "users",
    ],
)
@api_view(['POST'])
@permission_classes([AllowAny])
def sign_in_cookies(request: HttpRequest) -> HttpResponse:
    user = sign_in_core(request=request)
    return get_token_http_response(user)

    
@extend_schema(
    summary="WORKS: Logout",
    description="Take authenticated user's refresh token, revoke it and blacklist it",
    request=UserRefreshRequestSerializer,
    methods=["POST"],
    responses={
        204: OpenApiResponse(description="Successfully logged out."),
        400: OpenApiResponse(description="Error: Refresh token is required."),
        401: OpenApiResponse(description="Error: Authentication credentials were not provided."),
        422: OpenApiResponse(description="Error: Token is invalid or expired"),
    },
    tags=[
        "users",
    ],
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request: HttpRequest) -> HttpResponse:
    return blacklists_the_token(request=request)
    

# =============================================GET=============================================

    
@extend_schema(
    summary="WORKS: User's info",
    description="Takes id and returns user's info",
    methods=["GET"],
    responses={
        200: OpenApiResponse(response=UserInfoResponseSerializer),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "users",
    ]
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_info(request: HttpRequest) -> Response:
    response = get_user_info_core(request=request)
    return Response(response.data)
