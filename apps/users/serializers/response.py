from rest_framework import serializers

from ..models import UserModel


class SignInResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
    

class UserInfoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'email',
            'first_name',
            'last_name',
            'created_at',
        ]
    