# Generated by Django 4.2.1 on 2023-08-30 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0008_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='courses',
        ),
    ]
