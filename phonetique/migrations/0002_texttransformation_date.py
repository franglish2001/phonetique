# Generated by Django 5.1.4 on 2024-12-31 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonetique', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='texttransformation',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 12, 31, 13, 14, 42, 49644, tzinfo=datetime.timezone.utc)),
        ),
    ]