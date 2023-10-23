from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiParameter,
)

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.http import HttpRequest, HttpResponse

from ..core import get_items_user_core, get_item_info_core, create_item_core
from ..serializers import (
    ItemCreationRequestSerializer,
    ItemModelSerializer,
    ItemResponseSerializer,
)


# =============================================GET=============================================


@extend_schema(
    summary='WORKS: User Items',
    description='Returns a list of user items',
    methods=["GET"],
    responses={
        200: OpenApiResponse(response=ItemResponseSerializer(many=True)),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_items_user(request: HttpRequest) -> HttpResponse:
    response = get_items_user_core(request)
    return Response(response.data)


@extend_schema(
    summary='WORKS: Detailed description item',
    description='Returns a detailed description of the item',
    methods=["GET"],
    responses={
        200: OpenApiResponse(response=ItemResponseSerializer()),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_item_info(request: HttpRequest, item_id: int) -> HttpResponse:
    response = get_item_info_core(request, item_id) # отловить ошибку!!!
    return Response(response.data)


# =============================================POST=============================================

@extend_schema(
    summary="WORKS: Create item",
    description="Take item properties and create a new item.",
    request=ItemCreationRequestSerializer,
    methods=["POST"],
    responses={
        201: OpenApiResponse(description="Storage was successfully created"),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_item(request: HttpRequest) -> HttpResponse:
    response = create_item_core(request=request)
    return Response(response, status=status.HTTP_201_CREATED)
