# Generated by Django 4.1.6 on 2023-05-19 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdeposit',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_bank_deposit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankwithdrawal',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_banks_withdrawals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilemoneydeposit',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_momo_deposits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilemoneywithdraw',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_momo_withdrawals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paymentforrebalancing',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_payment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='addedtoapprovedpayment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_payments', to=settings.AUTH_USER_MODEL),
        ),
    ]
