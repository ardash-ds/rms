from typing import List

from django.http import HttpRequest

from ..models import CategoryModel

from ..serializers import CategoryModelSerializer


# =============================================GET=============================================


def get_category_core(request: HttpRequest) -> List[CategoryModel]:
    categories = CategoryModel.objects.all().order_by("name")
    return CategoryModelSerializer(categories, many=True)
