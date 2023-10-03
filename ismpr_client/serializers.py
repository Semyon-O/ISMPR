from rest_framework import serializers
from .models import Client, ClientEquipment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        Client.objects.create(user=new_user)
        return new_user


class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')


class ClientEquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientEquipment
        fields = ('client', 'Name', 'typeEquipment', 'Company', 'Description')
