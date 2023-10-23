from typing import List

from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404

from ..models import StorageModel

from ..serializers import StorageCreationRequestSerializer, StorageModelSerializer, StorageResponseSerializer


# =============================================GET=============================================

def get_storage_all_core(request: HttpRequest) -> List[StorageModel]:
    """Returns a list of StorageModel objects that belong to the request.users

    Parameters:
    - request (HttpRequest): A Django HttpRequest object.

    Returns:
    - List[StorageModel]: A list of all user StorageModel objects, sorted by name field.
      Serialized using the StorageResponseSerializer class.

    """
    storage = StorageModel.objects.filter(user__id=request.user.id).order_by("name")
    return StorageResponseSerializer(storage, many=True)


def get_storage_with_things_core(request: HttpRequest) -> List[StorageModel]:
    """Returns a list of StorageModel objects that belong to the request.users

    Parameters:
    - request (HttpRequest): A Django HttpRequest object.

    Returns:
    - List[StorageModel]: A list of StorageModel objects containing ItemModel 
      objects, sorted by name field. Serialized using the StorageResponseSerializer class.

    """
    storage = StorageModel.objects.filter(item_storage__user__id=request.user.id).order_by("name")
    return StorageResponseSerializer(storage, many=True)


# =============================================POST============================================

def create_storage_core(request: HttpRequest) -> None:
    """Create a new storage.

    Parameters:
    - request (HttpRequest): The HTTP request object containing the user.

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
    
    
# =============================================DELETE============================================
    
    
def delete_storage_core(request: HttpRequest, storage_id: int) -> dict:
    """Delete storage

    Args:
        request (HttpRequest): The HTTP request containing user authentication and authorization.
        storage_id (int): The ID of the storage to be deleted.

    Raises:
        code: 404 "Not found.". If the specified storage_id or user who submitted the deletion 
        request do not correspond to existing entities.

    Returns:
        dict: A dictionary containing a detail message indicating the success of the deletion.
    """
    
    storage = get_object_or_404(
        StorageModel, 
        id=storage_id, 
        user__id=request.user.id,
    )
    storage.delete()
    return {
        "detail": f"Storage (id:{storage_id}) was successfully deleted",
    }
    