# Generated by Django 4.0.10 on 2023-09-14 02:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customtoken_date_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtoken',
            name='date_expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 15, 2, 4, 32, 327927, tzinfo=utc)),
        ),
    ]
