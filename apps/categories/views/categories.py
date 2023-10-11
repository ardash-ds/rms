from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 
from rest_framework.permissions import IsAuthenticated as IsAuthenticated_

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
@permission_classes([AllowAny])
# @permission_classes([IsAuthenticated_])
def get_categories(request: HttpRequest) -> HttpResponse:
    response = get_category_core(request)
    http_response = HttpResponse(response.data)
    http_response.set_cookie('accessToken', "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJDb2RlU2FuZGJveCIsImV4cCI6MTY5NzQ1MDc1OCwiaWF0IjoxNjk1MDMxNTU4LCJpc3MiOiJDb2RlU2FuZGJveCIsImp0aSI6IjUxMDI5NjZjLTZlNmEtNDU4NS1iMmUwLTRhN2M2MjcxOGU3ZSIsIm5iZiI6MTY5NTAzMTU1Nywic3ViIjoiVXNlcjo0MDFkMDMyOC05MjFhLTRhOTktYTM2YS03YmVmZmRhOGFjNGIiLCJ0eXAiOiJyZWZyZXNoIn0.8flXgyQ9jdaAmCoMeaR4ZE3QiBhYVQQY7OrD0fcO6hDz15xGl6rLrGVvTNda0HSN96vP08Dap2hqjnAUgvUYQg", httponly=True, secure=True)
    return http_response
