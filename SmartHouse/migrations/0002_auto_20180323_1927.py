# Generated by Django 2.0.3 on 2018-03-23 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SmartHouse', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SmartHouseUsers',
            new_name='SmartHouseUser',
        ),
    ]