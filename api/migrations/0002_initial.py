# Generated by Django 4.1.6 on 2023-06-09 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='setupmeeting',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reports',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_reports', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reports',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='registeredforfloat',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joining_agent', to=settings.AUTH_USER_MODEL),
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
            model_name='paymentforrebalancing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_payment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ownermtnpayto',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_making_pay_to', to=settings.AUTH_USER_MODEL),
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
            model_name='mtnpayto',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='monthlypayments',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilemoneywithdraw',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilemoneywithdraw',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_momo_withdrawals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilemoneydeposit',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_requesting', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilemoneydeposit',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_momo_deposits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='holdaccounts',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admin_views', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='holdaccounts',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupownermessage',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupagentsmessage',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupagentsmessage',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_chatters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='freetrial',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fraud',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='floats',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='floats',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesting_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customeraccounts',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customer',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complains',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admin_complaining_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complains',
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
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_banks_withdrawals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankdeposit',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_requesting_bank', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankdeposit',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_bank_deposit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='authenticateagentphone',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentrequestpayment',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentrequestpayment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_receiving_payment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentrequestlimit',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentrequestlimit',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_setting_limit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentrequest',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentrequest',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentrebalancing',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rebalancing_agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentrebalancing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_rebalancing', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentaccountsbalancestarted',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentaccountsbalanceclosed',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentaccounts',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agentaccounts',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_creating_account', to=settings.AUTH_USER_MODEL),
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
        migrations.AddField(
            model_name='addedtoapprovedrequest',
            name='agent_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agentrequest'),
        ),
        migrations.AddField(
            model_name='addedtoapprovedrequest',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_request', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addedtoapprovedrebalancing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owners', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addedtoapprovedrebalancing',
            name='rebalancing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agentrebalancing'),
        ),
        migrations.AddField(
            model_name='addedtoapprovedpayment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents_owner_payments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addedtoapprovedpayment',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agentrequestpayment'),
        ),
    ]
