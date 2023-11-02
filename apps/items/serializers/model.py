from rest_framework import serializers  

from ..models import ItemModel, ItemImageModel


class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
        
        
class ItemImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImageModel
        fields = ['id', 'image_url']
        