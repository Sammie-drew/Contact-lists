
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=20, min_length=3)
    last_name = serializers.CharField(max_length=20, min_length=3)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email", ("Email already exist")})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(min_length=3)
    password = serializers.CharField(min_length=6)

    class Meta:
        model = User
        fields = ['username', 'password']
