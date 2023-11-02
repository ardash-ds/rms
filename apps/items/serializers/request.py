from rest_framework import serializers

from ..models import ItemModel, ItemImageModel


class ItemRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
        read_only_fields = ["user", 'created_at',]
        
        
class ItemPutRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = [
            'id',
            'name',
            'description',
            'category',
            'storage',
        ]
        read_only_fields = ["user", 'created_at',]


class ItemCreationRequestSerializer(serializers.Serializer):
    item = ItemRequestSerializer()
    image_list = serializers.ListField(
        child=serializers.ImageField(write_only=True), 
        required=False,
    )
    
    
class ItemImagRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImageModel
        fields = '__all__'
        read_only_fields = ['item', 'created_at',]
        
        
class ImageRequestSerializer(serializers.Serializer):
    images = serializers.ListField(child=serializers.ImageField())
    
    
    
class ItemUpdateRequestSerializer(serializers.Serializer):
    item = ItemRequestSerializer()
    image_list = serializers.ListField(
        child=serializers.ImageField(write_only=True), 
        required=False,
    )
    image_delete_list = serializers.ListField(
        child=serializers.IntegerField(write_only=True), 
        required=False,
    )
    