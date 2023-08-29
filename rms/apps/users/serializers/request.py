from rest_framework import serializers
from ..models import UserModel


class UserRegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'email', 
            'password',
        ]
        extra_kwargs = {
            "email": {"default": "user1@example.com"},
            "password": {"default": "qwerty1234"},
        }


class UserRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    