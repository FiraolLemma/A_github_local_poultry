# Generated by Django 5.2.1 on 2025-06-24 19:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='kvtec0mqxawgxmhsaamd', max_length=255, verbose_name='image'),
        ),
    ]
