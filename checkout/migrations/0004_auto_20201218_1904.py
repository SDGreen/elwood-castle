# Generated by Django 3.1.4 on 2020-12-18 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20201218_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventbooking',
            name='booking_total',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=7),
        ),
    ]