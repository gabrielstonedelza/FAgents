# Generated by Django 4.1.6 on 2023-08-04 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_abag_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='abag_code',
            new_name='agent_code',
        ),
    ]
