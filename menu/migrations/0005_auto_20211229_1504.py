# Generated by Django 3.2 on 2021-12-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_rename_com_name_components_name_com'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='components',
            name='meals',
        ),
        migrations.AddField(
            model_name='meals',
            name='components',
            field=models.ManyToManyField(to='menu.Components'),
        ),
    ]
