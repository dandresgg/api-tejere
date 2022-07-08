''' Profile model '''
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=20, null=True)
    phone = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user}, {self.user.email}"
