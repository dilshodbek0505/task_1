from rest_framework import serializers

from api.v1.utile.serializer import CustomAbstractSerializer
from .models import User


class UserSerializer(CustomAbstractSerializer):
    password = serializers.CharField(max_length = 255, write_only = True)
    repeate_password = serializers.CharField(max_length = 255, write_only = True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone", "email", "password", "repeate_password")
    
    def validate(self, attrs):
        data = super().validate(attrs)
        password1 = attrs['password']
        password2 = attrs['repeate_password']
        if not(password1 and password2) or (password1 != password2):
            raise serializers.ValidationError("Password not given or not mutch")
        return data

    def create(self, validated_data):
        password = validated_data.get("password")
        validated_data.pop("repeate_password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserUpdateSeriaizer(CustomAbstractSerializer):
    password = serializers.CharField(max_length = 255, write_only = True)
    
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone", "email", "password")
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        password = validated_data.get("password")
        print(password)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

