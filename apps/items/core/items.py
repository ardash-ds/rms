import json
import os
from typing import List

from django.conf import settings
from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from ..models import ItemModel, ItemImageModel
from core.exceptions import IncorrectFileFormatException

from ..serializers import (
    ItemResponseSerializer, 
    ItemRequestSerializer,
    ItemPutRequestSerializer,
    ImageRequestSerializer,
)


# =============================================GET=============================================

def get_items_core(request: HttpRequest) -> List[ItemModel]:
  
    """
    Retrieve a list user items
    
    Args:
    - request (HttpRequest): A Django HttpRequest object, containing user 
      authentication and authorization.
    
    Returns:
    - List[ItemModel]: A list of items objects.
    """
    
    items = ItemModel.objects.filter(user=request.user)
    return ItemResponseSerializer(items, many=True)


def get_item_info_core(request: HttpRequest, item_id: int) -> ItemModel:
    """
    Retrieve a detailed description of the item
    
    Args:
    - request (HttpRequest): A Django HttpRequest object, containing user 
      authentication and authorization.
    - item_id (int): ID of the object ItemModel whose data you want to get.  
    
    Returns:
    - ItemModel: Detailed description of the item.
    """
    
    item = get_object_or_404(ItemModel, id=item_id, user__id=request.user.id)
    images = ItemImageModel.objects.filter(item=item)
    # serialiser = ItemResponseSerializer(data=item)
    # serialiser.is_valid(raise_exception=True)
    # serialiser.validated_data['images'] = images
    # print('gggggg', ItemResponseSerializer(data=item, images=images))
    return ItemResponseSerializer(item)
# ============================================POST=============================================

@transaction.atomic
def create_item_core(request: HttpRequest) -> dict:
    """
    Create a new item.

    Args:
    - request (HttpRequest): A Django HttpRequest object, containing user 
      authentication and authorization.

    Returns:
    - ItemModel: Data of the created object ItemModel. Serialized using the 
      StorageResponseSerializer class.

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
        serializer_image = ImageRequestSerializer(data={'images': files})
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
def delete_item_core(request: HttpRequest, item_id: int) -> dict:
    """
    Deletes an item, as well as ItemImageModel objects and photo files 
    associated with this item.

    Args:
    - request (HttpRequest): A Django HttpRequest object, containing user 
      authentication and authorization.
    - item_id(int): ID of the object ItemModel to be deleted.

    Returns:
    - dict: A dictionary containing a detail message indicating 
      the success of the deletion.

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

# ============================================PUT=============================================


def update_item_core(request: HttpRequest, item_id: int) -> dict:
    data = request.data
    item = get_object_or_404(ItemModel, id=item_id)   # добавить user=request.user
    serialiser_item = ItemRequestSerializer(instance=item, data=json.loads(data.get('item')))
    serialiser_item.is_valid(raise_exception=True)
    serialiser_item.save()
    
    if data.get('image_delete_list'):
        image_delete_list = data.get('image_delete_list').split(',')
        print('dddd', ((image_delete_list)))
    
    
    files = request.FILES
    if files:
        serializer_image = ImageRequestSerializer(data={'images': files})
        serializer_image.is_valid(raise_exception=True)
        images = []
        for image in files.getlist('image_list'):
            if "image" not in image.content_type:
                raise IncorrectFileFormatException()
            item_image = ItemImageModel.objects.create(item=item, image_url=image)
            images.append(item_image.image_url.name)

    return ItemResponseSerializer(serialiser_item.instance).data

  