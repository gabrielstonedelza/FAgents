# Generated by Django 4.1.6 on 2023-04-22 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='privateusermessage',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatter2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='privateusermessage',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paymentforrebalancing',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notifications',
            name='notification_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notifications',
            name='notification_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_receiving_notification', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilemoneywithdraw',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilemoneywithdraw',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='momo_withdrawal_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilemoneydeposit',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_requesting', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilemoneydeposit',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='momo_deposit_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fraud',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fraud',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fraud_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customeraccounts',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customeraccounts',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_adding_accounts_to', to='api.customer'),
        ),
        migrations.AddField(
            model_name='customer',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankwithdrawal',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankwithdrawal',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_withdraw_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankdeposit',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_requesting_bank', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankdeposit',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_customer', to='api.customer'),
        ),
        migrations.AddField(
            model_name='agentsfloat',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesting_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentrebalancing',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rebalancing_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentaccounts',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addtoblocklist',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addtoblocklist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_being_blocked', to=settings.AUTH_USER_MODEL),
        ),
    ]
