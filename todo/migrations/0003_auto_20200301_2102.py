# Generated by Django 3.0.3 on 2020-03-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200301_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateField(default=True),
        ),
    ]
