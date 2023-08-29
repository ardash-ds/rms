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

from ..core import get_category_core
from ..serializers import (
    CategoryModelSerializer,
    CategoryResponseSerializer,
)


# =============================================GET=============================================


@extend_schema(
    summary='WORKS: Categories',
    description='Returns a list of all categories',
    methods=["GET"],
    request=None,
    responses={
        200: OpenApiResponse(response=CategoryModelSerializer(many=True))
    },
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request: HttpRequest) -> HttpResponse:
    response = get_category_core(request)
    return Response(response.data)
