from typing import List

from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest

from ..models import ItemModel
from apps.categories.models import CategoryModel

from ..serializers import (
    ItemModelSerializer,
    ItemResponseSerializer,
)

from apps.categories.serializers import CategoryModelSerializer


# =============================================GET=============================================

def get_items_user_core(request: HttpRequest) -> List[ItemModel]:
    items = ItemModel.objects.filter(user=request.user)
    return ItemResponseSerializer(items, many=True)


def get_item_info_core(request: HttpRequest, item_id: int) -> ItemModel:
    item = ItemModel.objects.get(id=item_id)
    return ItemResponseSerializer(item)
