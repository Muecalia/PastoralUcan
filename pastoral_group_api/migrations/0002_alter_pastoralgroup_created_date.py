# Generated by Django 5.1 on 2024-08-13 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastoral_group_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastoralgroup',
            name='created_date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 8, 13, 22, 2, 47, 847507, tzinfo=datetime.timezone.utc)),
        ),
    ]
