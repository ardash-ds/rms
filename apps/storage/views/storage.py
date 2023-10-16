from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiParameter,
)

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.http import HttpRequest, HttpResponse

from ..core import (
    create_storage_core,
    get_storage_all_core,
    get_storage_with_things_core,
)
from ..serializers import (
    StorageCreationRequestSerializer,
    StorageModelSerializer,
    StorageModelResponseSerializer,
)


# =============================================GET=============================================


@extend_schema(
    summary='WORKS: storage all',
    description='Returns a list of all storage the user',
    methods=["GET"],
    request=None,
    responses={
        200: OpenApiResponse(response=StorageModelResponseSerializer(many=True)),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_storage_all(request: HttpRequest) -> HttpResponse:
    response = get_storage_all_core(request)
    return Response(response.data)


@extend_schema(
    summary='WORKS: storage with things',
    description='Returns a list of storage with things the user',
    methods=["GET"],
    request=None,
    responses={
        200: OpenApiResponse(response=StorageModelResponseSerializer(many=True)),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_storage_with_things(request: HttpRequest) -> HttpResponse:
    response = get_storage_with_things_core(request)
    return Response(response.data)


# =============================================POST=============================================


@extend_schema(
    summary="WORKS: Create storage",
    description="Take storage properties and create a new storage.",
    request=StorageCreationRequestSerializer,
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
def create_storage(request: HttpRequest) -> HttpResponse:
    response = create_storage_core(request=request)
    return Response(status=status.HTTP_201_CREATED)
