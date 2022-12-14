''' Machines models '''
from django.db import models

KIND_MACHINE = [
    ('knitting', 'KNITTING'),
]

KIND_SECTOR = [
    ('upper_car', 'UPPER_CAR'),
    ('lower_car', 'LOWER_CAR'),
    ('needle_bed', 'NEEDLE_BED'),
    ('needle_selector', 'NEEDLE_SELECTOR'),
    ('transport_bag', 'TRANSPORT_BAG'),
    ('left_car', 'LEFT_CAR'),
    ('right_car', 'RIGHT_CAR'),
    ('accesories', 'ACCESORIES'),
]


class Machine(models.Model):
    ''' Machine model fields '''
    name = models.CharField(max_length=20,
                            unique=True)
    kind = models.CharField(choices=KIND_MACHINE,
                            max_length=20)

    def __str__(self):
        return f"{self.name} -- {self.kind} -- {self.pk}"


class Sector(models.Model):
    ''' Sector model fields '''
    machine = models.ForeignKey(Machine,
                                on_delete=models.CASCADE)
    kind = models.CharField(choices=KIND_SECTOR,
                            max_length=20)
    img = models.URLField(blank=False)

    def __str__(self):
        return f"{self.machine} -- {self.kind}"


class Part(models.Model):
    ''' Part model fields '''
    sector = models.ForeignKey(Sector,
                               on_delete=models.CASCADE)
    description = models.TextField(max_length=150,
                                   blank=False)
    code = models.CharField(max_length=20,
                            blank=False)
    reference = models.PositiveIntegerField(default=0,
                                            blank=False)
    price = models.DecimalField(default=0,
                                max_digits=10,
                                decimal_places=2,
                                blank=False)
    img = models.URLField(blank=False)
    photo = models.URLField(blank=False)
    url_seller = models.URLField(blank=False,
                                 default="",
                                 max_length=400)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['reference']

    def __str__(self):
        return f"{self.description}"
