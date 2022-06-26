from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from user_profile.models import Profile
from user_profile.serializers import ProfileSerializer,\
    UserSerializer, MyAuthTokenSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['GET'])
    def ask_superuser(self, request):
        user = request.user
        if user.is_superuser:
            return Response('true', status=status.HTTP_400_BAD_REQUEST)
        return Response('no admin', status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_id(self, request):
        user = request.user
        profile = Profile.objects.get(user=user)
        if not profile:
            return Response('no user', status=status.HTTP_400_BAD_REQUEST)
        return Response({'user_id': profile.id}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def update_profile(self, request):
        body = request.data['body']
        user = request.user
        profile = Profile.objects.get(user=user)
        if not body[0]:
            if body[0] == 'username':
                profile.user.username = body[1]
            if body[0] == 'email':
                profile.user.email = body[1]
            if body[0] == 'address':
                profile.address = body[1]
            if body[0] == 'phone':
                profile.phone = body[1]
            profile.save()
        if not profile:
            return Response('no user', status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    @action(detail=False, methods=["POST"])
    def send_msm(self, request):
        if not request.data['username']:
            return Response('Debes poner nombre', status=status.HTTP_400_BAD_REQUEST)
        if not request.data['email']:
            return Response('Debes poner un correo', status=status.HTTP_400_BAD_REQUEST)
        if not request.data['msm']:
            return Response('Debes poner un mensaje', status=status.HTTP_400_BAD_REQUEST)
        subject = f"Mensaje de {request.data['username']}"
        content = f"{request.data['email']}, escribe {request.data['msm']}"
        msm = EmailMultiAlternatives(subject,
                                     content,
                                     settings.EMAIL_HOST,
                                     [settings.EMAIL_HOST])
        # msm.attach_alternative(content, 'text/html')
        msm.send()
        return Response('done', status=status.HTTP_200_OK)


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
