# Generated by Django 5.2 on 2025-06-13 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_alter_booking_time_slot'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NonVegMenu200',
        ),
        migrations.DeleteModel(
            name='NonVegMenu250',
        ),
        migrations.DeleteModel(
            name='VegMenu150',
        ),
        migrations.DeleteModel(
            name='VegMenu200',
        ),
    ]
