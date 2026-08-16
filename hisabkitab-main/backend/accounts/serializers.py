from rest_framework import serializers
from django.contrib.auth import get_user_model
import logging

User = get_user_model()

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'shop_name', 'owner_name', 'phone']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'shop_name', 'owner_name', 'phone']

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                username=validated_data['email'],
                email=validated_data['email'],
                password=validated_data['password'],
                shop_name=validated_data['shop_name'],
                owner_name=validated_data['owner_name'],
                phone=validated_data['phone']
            )
            return user

        except Exception:
            logger.exception("SIGNUP ERROR")
            raise