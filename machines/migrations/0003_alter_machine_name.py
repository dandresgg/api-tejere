# Generated by Django 4.0.5 on 2022-06-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_sector_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
