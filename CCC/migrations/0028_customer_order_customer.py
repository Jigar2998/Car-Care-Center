# Generated by Django 3.1.5 on 2021-03-17 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0027_auto_20210314_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_order',
            name='Customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CCC.customer'),
            preserve_default=False,
        ),
    ]