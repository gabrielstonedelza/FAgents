# Generated by Django 4.1.6 on 2023-05-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_holdaccounts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mtnpayto',
            old_name='depositor_name',
            new_name='depositor_number',
        ),
        migrations.AlterField(
            model_name='agentaccountsbalanceclosed',
            name='date_closed',
            field=models.DateField(auto_now_add=True),
        ),
    ]
