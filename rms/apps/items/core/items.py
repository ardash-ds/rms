from typing import List

from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest

from ..models import ItemsModel

from ..serializers import (
    ItemsModelSerializer,
)


# =============================================GET=============================================

def get_items_core(request: HttpRequest) -> List[ItemsModel]:
    categories = ItemsModel.objects.all()
    return ItemsModelSerializer(categories, many=True)
