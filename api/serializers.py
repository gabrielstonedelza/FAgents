from rest_framework import serializers
from .models import Customer, CustomerAccounts, BankDeposit, MobileMoneyDeposit, MobileMoneyWithdraw, BankWithdrawal, PaymentForReBalancing, Reports, AddToBlockList, Fraud, AgentReBalancing, Notifications, AgentAccounts, AgentsFloat,PrivateChatId,PrivateUserMessage,GroupMessage,AgentPreregistration

class AgentPreregistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentPreregistration
        fields = ['id','name','phone_name','digital_address','date_registered']

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ['id','user','get_username','get_phone_number','get_date']
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
        fields = ['id','agent','customer','bank','account_number','account_name','amount','depositor_name','get_customer_name','get_customer_phone','get_agents_phone','get_agent_username','date_added','deposited_month','deposited_year','d_200','d_100','d_50','d_20','d_10','d_5','d_2','d_1','total']
        read_only_fields = ['agent']

class MomoDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileMoneyDeposit
        fields = ['id','agent','customer','network','amount','date_deposited','get_customer_name','get_customer_phone','get_agents_phone','get_agent_username','type','d_200','d_100','d_50','d_20','d_10','d_5','d_2','d_1','total']
        read_only_fields = ['agent']

class MomoWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileMoneyWithdraw
        fields = ['id','agent','customer','network','id_type','id_number','amount','date_of_withdrawal','get_customer_name','get_customer_phone','get_agents_phone','get_agent_username','d_200','d_100','d_50','d_20','d_10','d_5','d_2','d_1','total']
        read_only_fields = ['agent']

class BankWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankWithdrawal
        fields = ['id','agent','customer','bank','withdrawal_type','id_type','id_number','amount','date_of_withdrawal','get_customer_name','get_customer_phone','get_agents_phone','get_agent_username','d_200','d_100','d_50','d_20','d_10','d_5','d_2','d_1','total']
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