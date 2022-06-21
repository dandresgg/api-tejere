from django.db import models

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
                             null=True)
    bill = models.FileField(upload_to='bills/',
                            blank=True)
    send = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
