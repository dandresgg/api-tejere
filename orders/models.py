from django.db import models
from cloudinary.models import CloudinaryField

from user_profile.models import Profile

STATE = [
    ('no pago', 'NO PAGO'),
    ('revision', 'REVISION'),
    ('aprobado', 'APROBADO'),
]


class Order(models.Model):
    user = models.ForeignKey(Profile,
                             on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    data_json = models.JSONField(blank=True,
                                 default=dict)
    state = models.CharField(max_length=20,
                             choices=STATE,
                             default='no pago')
    bill = CloudinaryField('bills/',
                           blank=True,
                           resource_type='raw')
    send = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
