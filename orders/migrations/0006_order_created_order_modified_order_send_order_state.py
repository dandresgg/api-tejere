# Generated by Django 4.0.5 on 2022-06-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_data_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='send',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('no pago', 'NO PAGO'), ('revision', 'REVISION'), ('aprobado', 'APROBADO')], max_length=20, null=True),
        ),
    ]
