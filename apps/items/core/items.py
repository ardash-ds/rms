import json
import os
from typing import List

from rest_framework.parsers import JSONParser, DataAndFiles, MultiPartParser

from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.conf import settings
from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

from ..models import ItemModel, ItemImageModel
from apps.categories.models import CategoryModel
from core.exceptions import IncorrectFileFormatException

from ..serializers import (
    ItemCreationRequestSerializer,
    ItemImagRequestSerialiser,
    ItemResponseSerializer,
    ItemRequestSerializer,
    ImageRequestSerialiser,
)

from apps.categories.serializers import CategoryModelSerializer


# =============================================GET=============================================

def get_items_core(request: HttpRequest) -> List[ItemModel]:
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
    item = get_object_or_404(ItemModel, id=item_id, user__id=request.user.id)
    return ItemResponseSerializer(item)

# ============================================POST=============================================

@transaction.atomic
def create_item_core(request: HttpRequest) -> ItemModel:
    """Create a new item.

    Parameters:
    - request (HttpRequest): The HTTP request containing user authentication and authorization.

    Returns:
    - Object ItemModel.

    Raises:
    - ValidationError: If the data provided in the request is not valid.
    """

    data = request.data
    serialiser_item = ItemRequestSerializer(data=json.loads(data.get('item')))
    
    serialiser_item.is_valid(raise_exception=True)
    serialiser_item.validated_data["user"] = request.user
    item = serialiser_item.save()
    
    files = request.FILES
    if files:
        serializer_image = ImageRequestSerialiser(data={'images': files})
        serializer_image.is_valid(raise_exception=True)
        images = []
        for image in files.getlist('image_list'):
            if "image" not in image.content_type:
                raise IncorrectFileFormatException()
            item_image = ItemImageModel.objects.create(item=item, image_url=image)
            images.append(item_image.image_url.name)

    return ItemResponseSerializer(serialiser_item.instance).data


# ============================================DELETE=============================================


@transaction.atomic
def delete_item_core(request: HttpRequest, item_id: int) -> int:
    """Delete item.

    Parameters:
    - request (HttpRequest): The HTTP request containing user authentication and authorization.
    - item_id(int): ID of the item to be deleted.

    Returns:
    - dict: A dictionary containing a detail message indicating the success of the deletion.
              Example:
              {
                  "detail": "Item (id:{item_id}) was successfully deleted"
              } .

    Raises:
    - ValidationError: If the data provided in the request is not valid.
    """
    
    item = get_object_or_404(ItemModel, id=item_id, user__id=request.user.id)
    images = ItemImageModel.objects.filter(item__id=item_id)
    
    if images:
        for image in images:
            image_path = os.path.join(settings.MEDIA_ROOT, str(image.image_url))
            os.remove(image_path)
        images.delete()
    item.delete()
        
    return {
        "detail": f"Item (id:{item_id}) was successfully deleted",
    }
