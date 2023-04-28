# Generated by Django 4.1.6 on 2023-04-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_fraud_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentrebalancing',
            name='network',
            field=models.CharField(blank=True, choices=[('Select Network', 'Select Network'), ('Mtn', 'Mtn'), ('Tigo', 'Tigo'), ('AirtelTigo', 'AirtelTigo'), ('Vodafone', 'Vodafone')], default='Select Network', max_length=20),
        ),
        migrations.AlterField(
            model_name='bankwithdrawal',
            name='withdrawal_type',
            field=models.CharField(choices=[('Select Withdrawal Type', 'Select Withdrawal Type'), ('POS', 'POS'), ('Mobile App', 'Mobile App')], default='Cheque', max_length=120),
        ),
    ]