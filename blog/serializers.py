''' Blog serializers '''
from rest_framework import serializers

from blog.models import Post


class PostSerializers(serializers.ModelSerializer):
    ''' Serializer post model '''
    created = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Post
        fields = ('title', 'description', 'body', 'img', 'created')
