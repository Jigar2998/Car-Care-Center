# Generated by Django 3.0.5 on 2021-03-02 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0009_cus_request_orderid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cus_request',
            name='orderid',
        ),
    ]
