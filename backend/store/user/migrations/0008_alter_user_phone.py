# Generated by Django 4.2.6 on 2024-03-08 16:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]
