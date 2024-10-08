# Generated by Django 5.1 on 2024-08-10 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tb_country',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address_api.country')),
            ],
            options={
                'db_table': 'tb_province',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address_api.province')),
            ],
            options={
                'db_table': 'tb_county',
                'ordering': ['name'],
            },
        ),
    ]
