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
from ..serializers import CategoriesModelSerializer


# =============================================GET=============================================


@extend_schema(
    summary='WORKS: Categories',
    description='Returns a list of all categories',
    methods=["GET"],
    request=None,
    responses={
        200: OpenApiResponse(response=CategoriesModelSerializer),
        400: OpenApiResponse(description='Error: Bad request'),
        401: OpenApiResponse(description='Error: Unauthorized'),
        404: OpenApiResponse(description='Error: Not found'),
        422: OpenApiResponse(description='Error: Unprocessable entity'),
        500: OpenApiResponse(description='Error: Internal server error'),
    },
)
@api_view(['GET'])
def get_categories(request: HttpRequest) -> HttpResponse:
    response = get_categorie_core(request=request)
    return Response(response.data)
