# Generated by Django 3.0.3 on 2020-03-03 19:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_meetingitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingitem',
            name='due_time',
            field=models.TimeField(default=datetime.datetime(2020, 3, 3, 19, 0, 26, 884854, tzinfo=utc)),
        ),
    ]
