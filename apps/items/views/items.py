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

from ..core import get_items_user_core
from ..serializers import (
    ItemModelSerializer,
)


# =============================================GET=============================================


@extend_schema(
    summary='WORKS: User Items',
    description='Returns a list of user items',
    methods=["GET"],
    responses={
        200: OpenApiResponse(response=ItemModelSerializer(many=True)),
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
