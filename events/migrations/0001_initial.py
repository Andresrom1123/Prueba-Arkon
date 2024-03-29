# Generated by Django 3.2 on 2023-01-27 14:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('max_tickets', models.IntegerField(validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(1)])),
                ('start_at', models.DateField()),
                ('end_at', models.DateField()),
            ],
        ),
    ]
