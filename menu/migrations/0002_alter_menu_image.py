# Generated by Django 5.1.3 on 2025-02-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu/food_images'),
        ),
    ]
