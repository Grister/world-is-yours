# Generated by Django 4.2.6 on 2024-05-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_product_features_product_features_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productspecs',
            name='value',
            field=models.JSONField(blank=True, db_index=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='productspecs',
            name='value_en',
            field=models.JSONField(blank=True, db_index=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='productspecs',
            name='value_uk',
            field=models.JSONField(blank=True, db_index=True, default=list, null=True),
        ),
    ]
