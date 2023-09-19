from rest_framework import serializers


class CategoryResponseSerializer(serializers.Serializer):
    name = serializers.CharField()
    