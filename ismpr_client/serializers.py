from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Client, ClientEquipment, TypeEquipment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop("password")
        new_user: User = User(**validated_data)
        new_user.set_password(password)
        new_user.save()
        Client.objects.create(user=new_user)
        Token.objects.create(user=new_user)
        return new_user


class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')


class TypeEquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeEquipment
        fields = ('id', 'type', 'description')


class ClientShowEquipmentSerializer(serializers.ModelSerializer):
    typeEquipment = TypeEquipmentSerializer()

    class Meta:
        model = ClientEquipment
        fields = ('id', 'Name', 'typeEquipment', 'Company', 'Description')


class ClientEquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientEquipment
        fields = ('id', 'Name', 'typeEquipment', 'Company', 'Description')