from typing import List

from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest, HttpResponse

from ..models import StorageModel

from ..serializers import (
    StorageCreationRequestSerializer,
    StorageModelSerializer,
    StorageModelResponseSerializer,
)


# =============================================GET=============================================

def get_storage_all_core(request: HttpRequest) -> List[StorageModel]:
    """Returns a list of StorageModel objects that belong to the request.users

    Parameters:
    - request (HttpRequest): A Django HttpRequest object.

    Returns:
    - List[StorageModel]: A list of all user StorageModel objects, sorted by name field.
      Serialized using the StorageModelResponseSerializer class.

    """
    storage = StorageModel.objects.filter(user__id=request.user.id).order_by("name")
    return StorageModelResponseSerializer(storage, many=True)


def get_storage_with_things_core(request: HttpRequest) -> List[StorageModel]:
    """Returns a list of StorageModel objects that belong to the request.users

    Parameters:
    - request (HttpRequest): A Django HttpRequest object.

    Returns:
    - List[StorageModel]: A list of StorageModel objects containing ItemModel 
      objects, sorted by name field. Serialized using the StorageModelResponseSerializer class.

    """
    storage = StorageModel.objects.filter(item_storage__user__id=request.user.id).order_by("name")
    return StorageModelResponseSerializer(storage, many=True)


# =============================================POST============================================

def create_storage_core(request: HttpRequest) -> List[StorageModel]:
    """Create a new storage.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - None

    Raises:
    - ValidationError: If the data provided in the request is not valid.
    """
        
    data = JSONParser().parse(request)
    serializer = StorageCreationRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.validated_data["user"] = request.user
    serializer.save()
    
    
    