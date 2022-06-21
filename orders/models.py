from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    data = models.JSONField(blank=True)
    bill = models.FileField(upload_to='bills/',
                            blank=True)
