from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.http import HttpRequest, HttpResponse

from apps.categories.core import get_category_core
from apps.categories.serializers import CategoryModelSerializer
from core.services import IsAuthenticated

# =============================================GET=============================================


@extend_schema(
    summary='WORKS: Categories',
    description='Returns a list of all categories',
    methods=["GET"],
    # request=None,
    responses={
        200: OpenApiResponse(response=CategoryModelSerializer(many=True)),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(['GET'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def get_categories(request: HttpRequest) -> HttpResponse:
    response = get_category_core(request)
    return Response(response.data)
