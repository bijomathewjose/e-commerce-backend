# Generated by Django 4.1.7 on 2023-03-07 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=300)),
                ('price', models.FloatField()),
                ('image_url', models.URLField(max_length=2000, validators=[django.core.validators.URLValidator()])),
                ('stock', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='categories.categories')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
