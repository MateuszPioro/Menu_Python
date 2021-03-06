# Generated by Django 3.2 on 2021-12-29 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20211229_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('components', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.components')),
                ('meals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.meals')),
            ],
        ),
    ]
