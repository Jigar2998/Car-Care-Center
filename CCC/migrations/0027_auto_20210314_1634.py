# Generated by Django 3.0.5 on 2021-03-14 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0026_auto_20210314_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_order',
            old_name='Parts_Subcategory',
            new_name='Parts_Sub_Category',
        ),
    ]
