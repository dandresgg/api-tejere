# Generated by Django 4.0.5 on 2022-06-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0007_part_photo_alter_part_code_alter_part_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='photo',
            field=models.URLField(),
        ),
    ]
