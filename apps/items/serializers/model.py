from rest_framework import serializers  

from ..models import ItemModel


class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = "__all__"
        # fields = ['id', 'name',]
        