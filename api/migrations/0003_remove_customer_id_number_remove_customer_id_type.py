# Generated by Django 4.1.6 on 2023-04-25 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='id_type',
        ),
    ]
