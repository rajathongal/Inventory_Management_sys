# Generated by Django 2.1.2 on 2019-11-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0006_auto_20191115_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='barcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]