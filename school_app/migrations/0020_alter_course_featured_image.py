# Generated by Django 4.2.1 on 2024-06-10 10:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0019_video_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
