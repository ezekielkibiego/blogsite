# Generated by Django 4.2.7 on 2023-11-08 18:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='photo'),
        ),
    ]