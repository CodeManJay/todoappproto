# Generated by Django 3.0.3 on 2020-05-08 12:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_auto_20200426_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AlterField(
            model_name='meetingitem',
            name='due_time',
            field=models.TimeField(default=datetime.datetime(2020, 5, 8, 12, 5, 41, 456768, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='created',
            field=models.DateField(default='2020-05-08'),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
