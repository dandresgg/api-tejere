''' Blog views '''
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from blog.models import Post
from blog.serializers import PostSerializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (AllowAny, )
