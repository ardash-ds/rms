from rest_framework import serializers  

from ..models import ItemModel
from apps.categories.serializers import CategoryModelSerializer
from apps.storage.serializers import StorageResponseSerializer


class ItemResponseSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    storage = StorageResponseSerializer()
    class Meta:
        model = ItemModel
        fields = [
            'id', 
            'name', 
            'description', 
            'created_at', 
            'category', 
            'storage',
        ]
        