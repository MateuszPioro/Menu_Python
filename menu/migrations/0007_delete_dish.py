# Generated by Django 3.2 on 2021-12-29 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_dish'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dish',
        ),
    ]