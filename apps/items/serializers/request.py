from rest_framework import serializers

from .model import ItemModel


class ItemCreationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = "__all__"
        read_only_fields = [
            "user",
            "created_at",
        ]
        