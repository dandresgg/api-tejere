from django.shortcuts import render
from rest_framework import viewsets

from user_profile.models import Profile
from user_profile.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
