# Generated by Django 3.1 on 2020-09-08 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminderlist', '0014_auto_20200908_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likes',
        ),
    ]
