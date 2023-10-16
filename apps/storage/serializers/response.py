from rest_framework import serializers  

from ..models import StorageModel


class StorageModelResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageModel
        fields = ['id', 'name']
    