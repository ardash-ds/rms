from typing import List

from django.http import HttpRequest

from ..models import CategoryModel
from apps.items.models import ItemModel

from ..serializers import CategoryModelSerializer


# =============================================GET=============================================


def get_category_core(request: HttpRequest) -> List[CategoryModel]:
    categories = CategoryModel.objects.all()
    return CategoryModelSerializer(categories, many=True)


def get_categories_with_things_core(request: HttpRequest) -> List[CategoryModel]:
    categories = CategoryModel.objects.filter(item_category__user__id=request.user.id).order_by("name")
    return CategoryModelSerializer(categories, many=True)
