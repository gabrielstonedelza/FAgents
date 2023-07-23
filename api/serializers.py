from rest_framework import serializers
from .models import (Customer, CustomerAccounts, BankDeposit, MobileMoneyDeposit, MobileMoneyWithdraw, BankWithdrawal, Reports, AddToBlockList, Fraud,  Notifications, Floats, PrivateChatId, PrivateUserMessage, GroupMessage, AgentPreregistration, RegisteredForFloat, FreeTrial, MonthlyPayments, AuthenticateAgentPhone, MtnPayTo, SetUpMeeting, Complains, HoldAccounts,GroupOwnerMessage,AgentAndOwnerAccounts,GroupAgentsMessage,OwnerMtnPayTo,CheckAppVersion,CheckOwnerAppVersion,AgentAccounts)


class AgentAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentAccounts
        fields = ['id','agent','owner','account_number','account_name','mtn_linked_number','bank','date_added','phone','get_agent_username']
        read_only_fields = ['agent']

class AgentAndOwnerAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentAndOwnerAccounts
        fields = ['id','agent','account_number','account_name','mtn_linked_number','bank','date_added','phone']
        read_only_fields = ['agent']

class CheckAppVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckAppVersion
        fields = ['id','app_version','date_added']

class CheckOwnerAppVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOwnerAppVersion
        fields = ['id','app_version','date_added']

class OwnerMtnPayToSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerMtnPayTo
        fields = ['id','owner','agent_or_merchant','amount','reference','pay_to_type','date_added']
        read_only_fields = ['owner']
class GroupAgentsMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAgentsMessage
        fields = ['id','owner','agent','message','timestamp','get_agent_username']
class GroupOwnerMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupOwnerMessage
        fields = ['id','owner','message','timestamp','get_username','get_phone_number']
        read_only_fields = ['owner']


class HoldAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoldAccounts
        fields = ['id','administrator','agent','amount','customer_number','reason','date_added','merchant_id','transaction_id']
        read_only_fields =['agent']

class ComplainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complains
        fields = ['id','administrator','agent','title','complain','date_added','get_agent_username','get_agent_phone_number']
        read_only_fields = ['agent']

class SetUpMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetUpMeeting
        fields = ['id','administrator','title','message','date_of_meeting','time_of_meeting','date_created','meeting_link']
        read_only_fields = ['administrator']


class MtnPayToSerializer(serializers.ModelSerializer):
    class Meta:
        model = MtnPayTo
        fields = ['id','agent','customer','amount','pay_to_type','date_added','reference','depositor_number']
        read_only_fields = ['agent']
class RegisteredForFloatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredForFloat
        fields = ['id','agent','status','date_requested','get_agent_username','get_agent_code']
        read_only_fields = ['agent']

class AgentPreregistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentPreregistration
        fields = ['id','name','phone_number','digital_address','date_registered']

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ['id','user','message','timestamp','get_username','get_phone_number','get_date']
        read_only_fields = ['user']
class PrivateUserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateUserMessage
        fields = ['id','sender','receiver','private_chat_id','message','read','isSender','isReceiver','timestamp','get_senders_username','get_receivers_username']
class PrivateChatIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateChatId
        fields = ['id','chat_id','date_created']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','agent','name','phone','date_created','get_agents_phone','get_agent_username','unique_code','customer_pic','get_customer_pic']
        read_only_fields = ['agent']

class CustomerAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAccounts
        fields = ['id','agent','customer','account_number','account_name','bank','date_added','get_agents_phone','get_agent_username']
        read_only_fields = ['agent']

class BankDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDeposit
        fields = ['id','agent','owner','customer','bank','account_number','account_name','amount','depositor_name','depositor_number','get_agents_phone','get_agent_username','date_added','deposited_month','deposited_year',]
        read_only_fields = ['agent']
class MomoDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileMoneyDeposit
        fields = ['id','agent','owner','customer','network','amount_sent','date_deposited','get_agents_phone','get_agent_username','type','depositor_name','depositor_number','cash_received','deposited_month','deposited_year','d_date']
        read_only_fields = ['agent']
class MomoWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileMoneyWithdraw
        fields = ['id','agent','owner','customer','network','cash_paid','date_of_withdrawal','get_agents_phone','get_agent_username','amount_received',"withdrawal_month","withdrawal_year",'d_date']
        read_only_fields = ['agent']
class BankWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankWithdrawal
        fields = ['id','agent','owner','customer','bank','withdrawal_type','amount','date_of_withdrawal','get_agents_phone','get_agent_username','withdrawal_year','withdrawal_month']
        read_only_fields = ['agent']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['id','user','report','read','date_reported','time_reported','get_username','owner']
        read_only_fields = ['user']
class AddToBlockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToBlockList
        fields = ['id','user','date_blocked','get_username']
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['id','item_id','transaction_tag','notification_title','notification_message','read','notification_trigger','notification_from','notification_to','fraud_id','floating_id','report_id','payment_id','date_created',]


class AgentsFloatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floats
        fields = ['id','amount','paid','date_added','get_agents_phone','get_agent_username']
class FraudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fraud
        fields = ['id','agent','customer','reason','date_added','get_agents_username']
        read_only_fields = ['agent']


class AuthenticateAgentPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticateAgentPhone
        fields = ['id','agent','phone_id','phone_model','phone_brand','finger_print','phone_authenticated','date_authenticated','get_agent_unique_code','get_agent_username']
        read_only_fields = ['agent']

class FreeTrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeTrial
        fields = ['id','agent','start_date','end_date','date_started_trial','trial_started','trial_ended']
        read_only_fields = ['agent']

class MonthlyPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyPayments
        fields = ['id','agent','start_date','end_date','month_ended','date_added']