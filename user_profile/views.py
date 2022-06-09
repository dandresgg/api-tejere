from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema

from user_profile.models import Profile
from user_profile.serializers import ProfileSerializer, UserSerializer, MyAuthTokenSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class MyAuthToken(auth_views.ObtainAuthToken):
    serializer_class = MyAuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name='email',
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Email valido para autenticacion"
                    ),
                ),
                coreapi.Field(
                    name='password',
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Contrasena",
                        description="Contrasena valida para autenticacion"
                    ),
                ),
            ],
            encoding='application/json'
        )


obtain_auth_token = MyAuthToken.as_view()
