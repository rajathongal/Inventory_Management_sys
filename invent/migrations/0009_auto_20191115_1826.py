# Generated by Django 2.1.2 on 2019-11-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0008_auto_20191115_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='barcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
