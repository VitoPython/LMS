# Generated by Django 4.2.1 on 2023-08-30 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0011_remove_comment_name_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
