# Generated by Django 4.1.6 on 2023-05-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_agentaccounts_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setupmeeting',
            name='agent',
        ),
        migrations.AddField(
            model_name='holdaccounts',
            name='merchant_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='holdaccounts',
            name='transaction_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]