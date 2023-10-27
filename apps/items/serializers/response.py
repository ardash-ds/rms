from rest_framework import serializers  

from .model import ItemImageModelSerialiser
from ..models import ItemModel
from apps.categories.serializers import CategoryModelSerializer
from apps.storage.serializers import StorageResponseSerializer


class ItemResponseSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    storage = StorageResponseSerializer()
    created_at = serializers.DateField(format='%d.%m.%Y')
    images = ItemImageModelSerialiser(source="image_item_for_items", many=True)

    class Meta:
        model = ItemModel
        fields = [
            'id', 
            'name', 
            'description', 
            'created_at', 
            'category', 
            'storage',
            'images',
        ]
        