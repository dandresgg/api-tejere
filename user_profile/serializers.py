from django.contrib.auth.models import User
from django.core import validators
from django.db import reset_queries
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _, trim_whitespace

from user_profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'address', 'phone', 'document')


class UserSerializer(serializers.ModelSerializer):
    ''' create user registration '''
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('id',  'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        Token.objects.create(user=user)
        return user


class MyAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_('Email'))
    password = serializers.CharField(
        label=_("Password", ),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user_request = get_object_or_404(User, email=email)
            user = authenticate(username=user_request, password=password)
            if not user:
                msg = _('Correo y contrasena invalidos')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Debes incluir "Correo" y "contrasena".')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
