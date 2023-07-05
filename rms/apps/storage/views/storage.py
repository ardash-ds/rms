from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiParameter,
)

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.http import HttpRequest, HttpResponse

from ..core import get_storage_core
from ..serializers import (
    StorageModelSerializer
)


# =============================================GET=============================================


@extend_schema(
    summary='WORKS: storage',
    description='Returns a list of all storage',
    methods=["GET"],
    request=None,
    responses={
        200: OpenApiResponse(response=StorageModelSerializer(many=True))
    },
)
@api_view(['GET'])
def get_storage(request: HttpRequest) -> HttpResponse:
    response = get_storage_core(request)
    return Response(response.data)
