from rest_framework import serializers  

from ..models import ItemModel


class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
        