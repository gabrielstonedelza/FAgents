# Generated by Django 4.1.6 on 2023-05-12 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_rename_amount_paid_mobilemoneywithdraw_amount_received'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobilemoneywithdraw',
            name='customer_pic',
        ),
    ]