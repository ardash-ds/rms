from rest_framework import serializers  

from ..models import StorageModel


class StorageResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageModel
        fields = ['id', 'name']
    