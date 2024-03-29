# Generated by Django 3.2 on 2023-01-27 23:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=django.utils.timezone.now, auto_now_add=True)),
                ('redeemed', models.BooleanField(default=False)),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_tickets', to='events.event')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
