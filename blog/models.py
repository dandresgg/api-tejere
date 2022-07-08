''' Blog models '''
from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    ''' Post model '''
    title = models.CharField(max_length=30)
    description = RichTextField(null=True)
    body = RichTextField()
    img = models.URLField(null=True)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} + {self.created}"
