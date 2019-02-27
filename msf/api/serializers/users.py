# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

UserModel = get_user_model()


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel.objects.create(**validated_data)

        user.set_password(password)
        user.initialize()

        user.save()

        return user
