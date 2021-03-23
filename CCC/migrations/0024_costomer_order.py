# Generated by Django 3.0.5 on 2021-03-14 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0023_auto_20210312_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='costomer_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('oaddress', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('ordernote', models.CharField(max_length=100, null=True)),
                ('Parts_Subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CCC.parts_subcategory')),
            ],
        ),
    ]
