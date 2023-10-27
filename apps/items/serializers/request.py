from rest_framework import serializers

from ..models import ItemModel, ItemImageModel


class ItemRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
        read_only_fields = ["user", 'created_at',]


class ItemCreationRequestSerializer(serializers.Serializer):
    item = ItemRequestSerializer()
    image_list = serializers.ListField(
        child=serializers.ImageField(write_only=True), 
        required=False,
    )
    
    
class ItemImagRequestSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ItemImageModel
        fields = '__all__'
        read_only_fields = ['item', 'created_at',]
        
        
class ImageRequestSerialiser(serializers.Serializer):
    images = serializers.ListField(child=serializers.ImageField())
    