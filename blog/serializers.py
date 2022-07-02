from rest_framework import serializers
import datetime

from blog.models import Post


class PostSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Post
        fields = ('title', 'body', 'img', 'created')
