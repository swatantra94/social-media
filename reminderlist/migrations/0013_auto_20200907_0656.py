# Generated by Django 3.1 on 2020-09-07 06:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reminderlist', '0012_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todolist',
            new_name='Post',
        ),
    ]
