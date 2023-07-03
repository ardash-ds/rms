from rest_framework import serializers  

from ..models import CategoriesModel


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = '__all__'
        