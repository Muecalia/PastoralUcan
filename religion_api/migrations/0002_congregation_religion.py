# Generated by Django 5.1 on 2024-08-14 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('religion_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='congregation',
            name='religion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='religion_api.religion'),
        ),
    ]
