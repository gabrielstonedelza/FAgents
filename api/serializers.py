from rest_framework import serializers
from .models import Customer, CustomerAccounts, BankDeposit, MobileMoneyDeposit, MobileMoneyWithdraw, BankWithdrawal, PaymentForReBalancing, Reports, AddToBlockList, Fraud, AgentReBalancing, AuthenticatedPhoneAddress, Notifications, AgentAccounts, AgentsFloat

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','agent','name','location','digital_address','id_type','id_number','phone','date_of_birth','date_created','get_agents_phone','get_agent_username']
        read_only_fields = ['agent']

class CustomerAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAccounts
        fields = ['id','agent','customer','account_number','account_name','branch','bank','date_added','get_customer_name','get_customer_phone','get_agents_phone','get_agent_username']
        read_only_fields = ['agent']

class BankDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDeposit
        fields = ['id','agent','customer','bank','account_number','account_name','amount','get_customer_name','get_customer_phone','get_agents_phone','get_agent_username','date_added']
        read_only_fields = ['agent']

class MomoDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileMoneyDeposit
        fields = ['id','agent','customer','network','amount','charges','agent_commission','date_deposited','get_customer_name','get_customer_phone','get_agents_phone','get_agent_username']
        read_only_fields = ['agent']

class MomoWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileMoneyWithdraw
        fields = ['id','agent','customer','network','id_type','id_number','amount','charges','cash_out_commission','agent_commission','mtn_commission','date_of_withdrawal','get_customer_name','get_customer_phone','get_agents_phone','get_agent_username']
        read_only_fields = ['agent']

class BankWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankWithdrawal
        fields = ['id','agent','customer','bank','withdrawal_type','id_type','id_number','amount','date_of_withdrawal','get_customer_name','get_customer_phone','get_agents_phone','get_agent_username']
        read_only_fields = ['agent']


class PaymentForReBalancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentForReBalancing
        fields = ['id','agent','reason_for_payment','amount','transaction_id','payment_status','date_created','time_created','get_agent_username']
        read_only_fields = ['agent']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['id','user','report','read','date_reported','time_reported','get_username']
        read_only_fields = ['agent']

class AddToBlockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToBlockList
        fields = ['id','user','date_blocked','get_username']

class AuthenticatePhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticatedPhoneAddress
        fields = ['id','agent','phones_id','phone_model','phone_brand','finger_print','authenticated_phone','date_authenticated','get_username']
        read_only_fields = ['agent']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['id','item_id','transaction_tag','notification_title','notification_message','read','notification_trigger','notification_from','notification_to','fraud_id','floating_id','report_id','payment_id','date_created','notification_from_agent_username','notification_to_agent_username','get_notification_from_pic','get_notification_to_pic']

class AgentReBalancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentReBalancing
        fields = ['id','agent','amount','bank','account_number','account_name','branch','date_requested','get_agents_phone','get_agent_username']

class AgentAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentAccounts
        fields = ['id','agent','account_number','account_name','branch','bank','date_added','get_agents_phone','get_agent_username']
        read_only_fields = ['agent']

class AgentsFloatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentsFloat
        fields = ['id','amount','paid','date_added','get_agents_phone','get_agent_username']

class FraudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fraud
        fields = ['id','agent','customer','reason','date_added','get_customer_name','get_customer_phone','get_agents_username']
        read_only_fields = ['agent']