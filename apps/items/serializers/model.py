from rest_framework import serializers  

from ..models import ItemModel, ItemImageModel


class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
        
        
class ItemImageModelSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ItemImageModel
        fields = ['image_url']
        