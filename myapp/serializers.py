from rest_framework import serializers
from .models import CustomUser
from .models import UserRating
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'score']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'score']


User = get_user_model()


class CustomUserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['score']  # Только поле рейтинга, если нужно обновить только его

    def update(self, instance, validated_data):
        instance.score = validated_data.get('score', instance.score)
        instance.save()
        return instance

