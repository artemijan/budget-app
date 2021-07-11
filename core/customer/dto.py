# Serializers define the API representation.
from rest_framework import serializers

from core.customer.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'is_staff')


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
