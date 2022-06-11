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
    name = models.CharField(max_length=20)
    kind = models.CharField(choices=KIND_MACHINE,
                            max_length=20)

    def __str__(self):
        return f"{self.name} -- {self.kind}"


class Sector(models.Model):
    machine = models.ForeignKey(Machine,
                                on_delete=models.CASCADE)
    kind = models.CharField(choices=KIND_SECTOR,
                            max_length=20)

    def __str__(self):
        return f"{self.machine} -- {self.kind}"


class Part(models.Model):
    sector = models.ForeignKey(Sector,
                               on_delete=models.CASCADE)
    description = models.TextField(max_length=150,
                                   blank=True)
    code = models.CharField(max_length=20,
                            blank=True)
    reference = models.PositiveIntegerField(default=0,
                                            blank=True)
    price = models.DecimalField(default=0,
                                max_digits=10,
                                decimal_places=2)
    img = models.URLField(blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.description}"
