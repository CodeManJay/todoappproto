# Generated by Django 3.0.3 on 2020-05-16 12:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0022_auto_20200516_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingitem',
            name='due_time',
            field=models.TimeField(default=datetime.datetime(2020, 5, 16, 12, 47, 37, 875947, tzinfo=utc)),
        ),
    ]
