from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiParameter,
)

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.http import HttpRequest, HttpResponse

from ..core import get_categorie_core
from ..serializers import (
    CategoriesModelSerializer,
    CategoryResponseSerializer,
)


# =============================================GET=============================================


@extend_schema(
    summary='WORKS: Categories',
    description='Returns a list of all categories',
    methods=["GET"],
    request=None,
    responses={
        200: OpenApiResponse(response=CategoriesModelSerializer(many=True))
    },
)
@api_view(['GET'])
def get_categories(request: HttpRequest) -> HttpResponse:
    response = get_categorie_core(request)
    return Response(response.data)
