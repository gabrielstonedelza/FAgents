# Generated by Django 4.1.6 on 2023-07-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_requestfloat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestfloat',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='requestfloat',
            name='exchange_for',
        ),
        migrations.RemoveField(
            model_name='requestfloat',
            name='float_to_exchange',
        ),
        migrations.AddField(
            model_name='requestfloat',
            name='float_request',
            field=models.CharField(default='', max_length=255),
        ),
    ]