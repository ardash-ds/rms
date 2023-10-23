from typing import List

from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from ..models import ItemModel
from apps.categories.models import CategoryModel

from ..serializers import (
    ItemCreationRequestSerializer,
    ItemModelSerializer,
    ItemResponseSerializer,
)

from apps.categories.serializers import CategoryModelSerializer


# =============================================GET=============================================

def get_items_user_core(request: HttpRequest) -> List[ItemModel]:
    """
    Retrieve a list user items
    
    Args:
        request (HttpRequest): The HTTP request containing user authentication and authorization.
    
    Returns:
        List[ItemModel]: A list of items objects.
    """
    
    items = ItemModel.objects.filter(user=request.user)
    return ItemResponseSerializer(items, many=True)


def get_item_info_core(request: HttpRequest, item_id: int) -> ItemModel:
    """
    Retrieve a detailed description of the item
    
    Args:
        request (HttpRequest): The HTTP request containing user authentication and authorization.
    
    Returns:
        ItemModel: Detailed description of the item.
    """
    item = get_object_or_404(id=item_id, user__id=request.user.id)
    return ItemResponseSerializer(item)

# ============================================POST=============================================

def create_item_core(request: HttpRequest) -> ItemModel:
    """Create a new item.

    Parameters:
    - request (HttpRequest): The HTTP request containing user authentication and authorization.

    Returns:
    - Object ItemModel.

    Raises:
    - ValidationError: If the data provided in the request is not valid.
    """
    
    data = JSONParser().parse(request)
    serializer = ItemCreationRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.validated_data["user"] = request.user
    serializer.save()
    
    return ItemResponseSerializer(serializer.instance).data
