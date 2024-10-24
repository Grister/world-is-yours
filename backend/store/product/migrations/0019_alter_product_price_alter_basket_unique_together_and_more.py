# Generated by Django 4.2.6 on 2024-03-10 11:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0018_rename_image_product_image_1_product_image_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=8),
        ),
        migrations.AlterUniqueTogether(
            name='basket',
            unique_together={('user', 'product')},
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['price'], name='price_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['category'], name='category_idx'),
        ),
    ]
