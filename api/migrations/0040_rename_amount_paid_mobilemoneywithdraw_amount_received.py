# Generated by Django 4.1.6 on 2023-05-12 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_mobilemoneywithdraw_amount_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobilemoneywithdraw',
            old_name='amount_paid',
            new_name='amount_received',
        ),
    ]