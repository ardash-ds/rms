from typing import List

from django.http import HttpRequest

from ..models import CategoryModel
from ..serializers import CategoryModelSerializer


# =============================================GET=============================================


def get_category_all_core(request: HttpRequest) -> List[CategoryModel]:
    """Get a list of CategoryModel objects.

    Args:
    - request (HttpRequest): A Django HttpRequest object, containing user 
      authentication and authorization.

    Returns:
    - List[CategoryModel]: A list of CategoryModel objects, sorted by name field.

    """
    
    return CategoryModelSerializer(CategoryModel.objects.all(), many=True)


def get_categories_with_things_core(request: HttpRequest) -> List[CategoryModel]:
    """Get a list of CategoryModel objects that are contained in ItemModel objects of a given user.

    Args:
    - request (HttpRequest): A Django HttpRequest object, containing user 
      authentication and authorization.

    Returns:
    - List[CategoryModel]: A list of CategoryModel objects, sorted by name field.

    """
    
    return CategoryModelSerializer(
        CategoryModel.objects.filter(
            item_category__user__id=request.user.id
        ).distinct().order_by("name"), 
        many=True,
    )
