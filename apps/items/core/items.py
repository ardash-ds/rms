from typing import List

from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest

from ..models import ItemModel
from apps.categories.models import CategoryModel

from ..serializers import (
    ItemModelSerializer,
)

from apps.categories.serializers import CategoryModelSerializer


# =============================================GET=============================================

def get_items_user_core(request: HttpRequest) -> List[ItemModel]:
    items = ItemModel.objects.filter(user=request.user)
    return ItemModelSerializer(items, many=True)
