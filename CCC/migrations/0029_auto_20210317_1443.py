# Generated by Django 3.1.5 on 2021-03-17 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0028_customer_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_order',
            name='Parts_Sub_Category',
        ),
        migrations.AddField(
            model_name='customer_order',
            name='product',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
