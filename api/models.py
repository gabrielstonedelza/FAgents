from email.policy import default

from django.db import models
from django.conf import settings
from django.utils import timezone
from decimal import Decimal
from django.utils.text import slugify
from datetime import datetime
from users.models import DeUser, SupervisorProfile, AdminProfile, AgentProfile
from django.contrib.humanize.templatetags import humanize

User = settings.AUTH_USER_MODEL

ID_TYPES = (
    ("Select Id Type", "Select Id Type"),
    ("Ghana Card", "Ghana Card"),
    ("Passport", "Passport"),
    ("Drivers License", "Drivers License"),
    ("Voters Id", "Voters Id"),
)
BANK_REDRAW_ID_TYPES = (
    ("Select Withdrawal Type", "Select Withdrawal Type"),
    ("Cheque", "Cheque"),
    ("Atm", "Atm"),
    ("Phone", "Phone"),
)
BANKS = (
    ("Select bank", "Select bank"),
    ("Access Bank", "Access Bank"),
    ("Cal Bank", "Cal Bank"),
    ("Fidelity Bank", "Fidelity Bank"),
    ("Ecobank", "Ecobank"),
    ("Adansi rural bank", "Adansi rural bank"),
    ("Kwumawuman Bank", "Kwumawuman Bank"),
    ("Pan Africa", "Pan Africa"),
    ("SGSSB", "SGSSB"),
    ("Atwima Rural Bank", "Atwima Rural Bank"),
    ("Omnibsic Bank", "Omnibsic Bank"),
    ("Omini bank", "Omini bank"),
    ("Stanbic Bank", "Stanbic Bank"),
    ("First Bank of Nigeria", "First Bank of Nigeria"),
    ("Adehyeman Savings and loans", "Adehyeman Savings and loans",),
    ("ARB Apex Bank Limited", "ARB Apex Bank Limited",),
    ("Absa Bank", "Absa Bank"),
    ("Agriculture Development bank", "Agriculture Development bank"),
    ("Bank of Africa", "Bank of Africa"),
    ("Bank of Ghana", "Bank of Ghana"),
    ("Consolidated Bank Ghana", "Consolidated Bank Ghana"),
    ("First Atlantic Bank", "First Atlantic Bank"),
    ("First National Bank", "First National Bank"),
    ("G-Money", "G-Money"),
    ("GCB BanK LTD", "GCB BanK LTD"),
    ("Ghana Pay", "Ghana Pay"),
    ("GHL Bank Ltd", "GHL Bank Ltd"),
    ("GT Bank", "GT Bank"),
    ("National Investment Bank", "National Investment Bank"),
    ("Opportunity International Savings And Loans", "Opportunity International Savings And Loans"),
    ("Prudential Bank", "Prudential Bank"),
    ("Republic Bank Ltd", "Republic Bank Ltd"),
    ("Sahel Sahara Bank", "Sahel Sahara Bank"),
    ("Sinapi Aba Savings and Loans", "Sinapi Aba Savings and Loans"),
    ("Societe Generale Ghana Ltd", "Societe Generale Ghana Ltd"),
    ("Standard Chartered", "Standard Chartered"),
    ("universal Merchant Bank", "universal Merchant Bank"),
    ("Zenith Bank", "Zenith Bank"),
    ("Mtn", "Mtn"),
    ("AirtelTigo", "AirtelTigo"),
    ("Vodafone", "Vodafone"),
)

NETWORKS = (
    ("Select Network", "Select Network"),
    ("Mtn", "Mtn"),
    ("Tigo", "Tigo"),
    ("AirtelTigo", "AirtelTigo"),
    ("Vodafone", "Vodafone"),
)

DEPOSIT_REQUEST_OPTIONS = (
    ("Cash", "Cash"),
    ("Mobile Money", "Money Money"),
    ("Bank", "Bank"),
)

MOBILE_MONEY_DEPOSIT_TYPE = (
    ("Loading", "Loading"),
    ("Direct", "Direct"),
    ("Agent to Agent", "Agent to Agent"),
)

MOBILE_MONEY_ACTION = (
    ("Deposit", "Deposit"),
    ("Withdraw", "Withdraw"),
)

WITHDRAW_TYPES = (
    ("MomoPay", "MomoPay"),
    ("Cash Out", "Cash Out"),
    ("Agent to Agent", "Agent to Agent"),
)

PAYMENT_STATUS = (
    ("Approved", "Approved"),
    ("Pending", "Pending"),
    ("Rejected", "Rejected")
)

REQUEST_PAID_OPTIONS = (
    ("Not Paid", "Not Paid"),
    ("Paid", "Paid"),
)

NOTIFICATIONS_STATUS = (
    ("Read", "Read"),
    ("Not Read", "Not Read"),
)

NOTIFICATIONS_TRIGGERS = (
    ("Triggered", "Triggered"),
    ("Not Triggered", "Not Triggered"),
)


class Customer(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    location = models.CharField(max_length=100, blank=True)
    digital_address = models.CharField(max_length=25, blank=True)
    id_type = models.CharField(max_length=50, choices=ID_TYPES, blank=True, default="Passport")
    id_number = models.CharField(max_length=50, blank=True, default="")
    phone = models.CharField(max_length=15, unique=True, blank=True)
    date_of_birth = models.CharField(max_length=15, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_agents_phone(self):
        return self.agent.phone

    def get_agent_username(self):
        return self.agent.username


class CustomerAccounts(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_adding_accounts_to")
    account_number = models.CharField(max_length=16, blank=True)
    account_name = models.CharField(max_length=100, blank=True)
    bank = models.CharField(max_length=100, choices=BANKS, default="Access Bank")
    branch = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone

    def get_customer_name(self):
        return self.customer.name

    def get_customer_phone(self):
        return self.customer.phone

    def get_agents_phone(self):
        return self.agent.phone

    def get_agent_username(self):
        return self.agent.username


class BankDeposit(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agent_requesting_bank")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="bank_customer")
    bank = models.CharField(max_length=50, choices=BANKS, blank=True, default="")
    account_number = models.TextField(blank=True, max_length=17)
    account_name = models.CharField(max_length=100, blank=True, default="")
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=19, default=0.0)
    d_200 = models.IntegerField(default=0, blank=True)
    d_100 = models.IntegerField(default=0, blank=True)
    d_50 = models.IntegerField(default=0, blank=True)
    d_20 = models.IntegerField(default=0, blank=True)
    d_10 = models.IntegerField(default=0, blank=True)
    d_5 = models.IntegerField(default=0, blank=True)
    d_2 = models.IntegerField(default=0, blank=True)
    d_1 = models.IntegerField(default=0, blank=True)
    depositor_name = models.CharField(max_length=50, blank=True, default="")
    deposited_month = models.CharField(max_length=10, blank=True, default="")
    deposited_year = models.CharField(max_length=10, blank=True, default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        two_h_cedis_values = self.d_200 * 200
        one_h_cedis_values = self.d_100 * 100
        fifty_cedis_values = self.d_50 * 50
        twenty_cedis_values = self.d_20 * 20
        ten_cedis_values = self.d_10 * 10
        five_cedis_values = self.d_5 * 5
        two_cedis_values = self.d_2 * 2
        one_cedi_values = self.d_1 * 1

        amount_total = Decimal(two_h_cedis_values) + Decimal(one_h_cedis_values) + Decimal(
            fifty_cedis_values) + Decimal(
            twenty_cedis_values) + Decimal(ten_cedis_values) + Decimal(five_cedis_values) + Decimal(
            two_cedis_values) + Decimal(one_cedi_values)
        self.total = Decimal(amount_total)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer.name

    def get_customer_name(self):
        return self.customer.name

    def get_customer_phone(self):
        return self.customer.phone

    def get_agents_phone(self):
        return self.agent.phone

    def get_agent_username(self):
        return self.agent.username


class MobileMoneyDeposit(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agent_requesting")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="momo_deposit_customer")
    depositor_name = models.CharField(max_length=30, blank=True, default="")
    depositor_number = models.CharField(max_length=30, blank=True, default="")
    reference = models.CharField(max_length=100, blank=True, default="")
    network = models.CharField(max_length=20, choices=NETWORKS, blank=True, default="Select Network")
    type = models.CharField(max_length=20, blank=True, choices=MOBILE_MONEY_DEPOSIT_TYPE)
    total = models.DecimalField(decimal_places=2, max_digits=19, default=0.0)
    d_200 = models.IntegerField(default=0, blank=True)
    d_100 = models.IntegerField(default=0, blank=True)
    d_50 = models.IntegerField(default=0, blank=True)
    d_20 = models.IntegerField(default=0, blank=True)
    d_10 = models.IntegerField(default=0, blank=True)
    d_5 = models.IntegerField(default=0, blank=True)
    d_2 = models.IntegerField(default=0, blank=True)
    d_1 = models.IntegerField(default=0, blank=True)
    date_deposited = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        two_h_cedis_values = self.d_200 * 200
        one_h_cedis_values = self.d_100 * 100
        fifty_cedis_values = self.d_50 * 50
        twenty_cedis_values = self.d_20 * 20
        ten_cedis_values = self.d_10 * 10
        five_cedis_values = self.d_5 * 5
        two_cedis_values = self.d_2 * 2
        one_cedi_values = self.d_1 * 1

        amount_total = Decimal(two_h_cedis_values) + Decimal(one_h_cedis_values) + Decimal(
            fifty_cedis_values) + Decimal(
            twenty_cedis_values) + Decimal(ten_cedis_values) + Decimal(five_cedis_values) + Decimal(
            two_cedis_values) + Decimal(one_cedi_values)
        self.total = Decimal(amount_total)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Mobile money request made for {self.amount}"

    def get_customer_name(self):
        return self.customer.name

    def get_customer_phone(self):
        return self.customer.phone

    def get_agents_phone(self):
        return self.agent.phone

    def get_agent_username(self):
        return self.agent.username


class MobileMoneyWithdraw(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="momo_withdrawal_customer")
    # customer_name = models.CharField(max_length=30, blank=True)
    network = models.CharField(max_length=20, choices=NETWORKS, blank=True, default="Select Network")
    id_type = models.CharField(max_length=30, choices=ID_TYPES)
    id_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True)

    total = models.DecimalField(decimal_places=2, max_digits=19, default=0.0)
    d_200 = models.IntegerField(default=0, blank=True)
    d_100 = models.IntegerField(default=0, blank=True)
    d_50 = models.IntegerField(default=0, blank=True)
    d_20 = models.IntegerField(default=0, blank=True)
    d_10 = models.IntegerField(default=0, blank=True)
    d_5 = models.IntegerField(default=0, blank=True)
    d_2 = models.IntegerField(default=0, blank=True)
    d_1 = models.IntegerField(default=0, blank=True)
    date_of_withdrawal = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        two_h_cedis_values = self.d_200 * 200
        one_h_cedis_values = self.d_100 * 100
        fifty_cedis_values = self.d_50 * 50
        twenty_cedis_values = self.d_20 * 20
        ten_cedis_values = self.d_10 * 10
        five_cedis_values = self.d_5 * 5
        two_cedis_values = self.d_2 * 2
        one_cedi_values = self.d_1 * 1

        amount_total = Decimal(two_h_cedis_values) + Decimal(one_h_cedis_values) + Decimal(
            fifty_cedis_values) + Decimal(
            twenty_cedis_values) + Decimal(ten_cedis_values) + Decimal(five_cedis_values) + Decimal(
            two_cedis_values) + Decimal(one_cedi_values)
        self.total = Decimal(amount_total)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Withdrawal made for {self.amount}"

    def get_customer_name(self):
        return self.customer.name

    def get_customer_phone(self):
        return self.customer.phone

    def get_agents_phone(self):
        return self.agent.phone

    def get_agent_username(self):
        return self.agent.username


class BankWithdrawal(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bank_withdraw_customer")
    bank = models.CharField(max_length=100, choices=BANKS, default="GT Bank")
    withdrawal_type = models.CharField(max_length=120, choices=BANK_REDRAW_ID_TYPES, default="Cheque")
    id_type = models.CharField(max_length=20, choices=ID_TYPES)
    id_number = models.CharField(max_length=20, default="0")
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(decimal_places=2, max_digits=19, default=0.0)
    d_200 = models.IntegerField(default=0, blank=True)
    d_100 = models.IntegerField(default=0, blank=True)
    d_50 = models.IntegerField(default=0, blank=True)
    d_20 = models.IntegerField(default=0, blank=True)
    d_10 = models.IntegerField(default=0, blank=True)
    d_5 = models.IntegerField(default=0, blank=True)
    d_2 = models.IntegerField(default=0, blank=True)
    d_1 = models.IntegerField(default=0, blank=True)
    date_of_withdrawal = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        two_h_cedis_values = self.d_200 * 200
        one_h_cedis_values = self.d_100 * 100
        fifty_cedis_values = self.d_50 * 50
        twenty_cedis_values = self.d_20 * 20
        ten_cedis_values = self.d_10 * 10
        five_cedis_values = self.d_5 * 5
        two_cedis_values = self.d_2 * 2
        one_cedi_values = self.d_1 * 1

        amount_total = Decimal(two_h_cedis_values) + Decimal(one_h_cedis_values) + Decimal(
            fifty_cedis_values) + Decimal(
            twenty_cedis_values) + Decimal(ten_cedis_values) + Decimal(five_cedis_values) + Decimal(
            two_cedis_values) + Decimal(one_cedi_values)
        self.total = Decimal(amount_total)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Withdrawal made for {self.amount} by {self.agent.username}"

    def get_customer_name(self):
        return self.customer.name

    def get_customer_phone(self):
        return self.customer.phone

    def get_agents_phone(self):
        return self.agent.phone

    def get_agent_username(self):
        return self.agent.username


class Reports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.TextField()
    read = models.BooleanField(default=False)
    date_reported = models.DateField(auto_now_add=True)
    time_reported = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username


class AddToBlockList(models.Model):
    administrator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_being_blocked")
    date_blocked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username


class Fraud(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fraud_customer")
    reason = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_customer_name(self):
        return self.customer.name

    def get_customer_phone(self):
        return self.customer.phone

    def get_agents_username(self):
        return self.agent.username


class PaymentForReBalancing(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0, blank=True)
    transaction_id = models.CharField(max_length=30, blank=True, default="")
    reason_for_payment = models.CharField(max_length=200)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS, default="Pending")
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)

    def __str__(self):
        if self.payment_status == "Pending":
            return f"{self.agent.username}'s payment is pending"
        return f"{self.agent.username}'s payment is approved"

    def get_agents_username(self):
        return self.agent.username


class AgentReBalancing(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rebalancing_agent")
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0, blank=True)
    bank = models.CharField(max_length=50, choices=BANKS, blank=True, default="")
    account_number = models.CharField(max_length=16, blank=True)
    account_name = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def get_agent_requesting_username(self):
        return self.agent1.username

    def get_agent_accepting_username(self):
        return self.agent2.username


class AgentAccounts(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=16, blank=True)
    account_name = models.CharField(max_length=100, blank=True)
    bank = models.CharField(max_length=100, choices=BANKS, default="Access Bank")
    branch = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.username

    def get_agents_phone(self):
        return self.agent.phone

    def get_agent_username(self):
        return self.agent.username


class Notifications(models.Model):
    item_id = models.CharField(max_length=100, blank=True, default="")
    transaction_tag = models.CharField(max_length=100, blank=True, default="")
    notification_title = models.CharField(max_length=200, blank=True)
    notification_message = models.TextField(blank=True)
    read = models.CharField(max_length=20, choices=NOTIFICATIONS_STATUS, default="Not Read")
    notification_trigger = models.CharField(max_length=100, choices=NOTIFICATIONS_TRIGGERS, default="Triggered",
                                            blank=True)
    notification_from = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    notification_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User_receiving_notification",
                                        null=True)

    fraud_id = models.CharField(max_length=100, blank=True)
    floating_id = models.CharField(max_length=100, blank=True)
    report_id = models.CharField(max_length=100, blank=True)
    payment_id = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title

    def notification_from_agent_username(self):
        return self.notification_from.username

    def notification_to_agent_username(self):
        return self.notification_to.username

    def get_notification_from_pic(self):
        my_user = User.objects.get(username=self.notification_from.username)
        if my_user.user_type == "Supervisor":
            my_supervisor = SupervisorProfile.objects.get(user=self.notification_from)
            if my_supervisor:
                return "http://127.0.0.1:8000" + my_supervisor.profile_pic.url
            return ""

        if my_user.user_type == "Agent":
            my_agent = AgentProfile.objects.get(user=self.notification_from)
            if my_agent:
                return "http://127.0.0.1:8000" + my_agent.profile_pic.url
            return ""

        if my_user.user_type == "Administrator":
            administrator = AdminProfile.objects.get(user=self.notification_from)
            if administrator:
                return "http://127.0.0.1:8000" + administrator.profile_pic.url
            return ""

    def get_notification_to_pic(self):
        my_user = User.objects.get(username=self.notification_to.username)
        if my_user.user_type == "Supervisor":
            my_supervisor = SupervisorProfile.objects.get(user=self.notification_to)
            if my_supervisor:
                return "http://127.0.0.1:8000" + my_supervisor.profile_pic.url
            return ""

        if my_user.user_type == "Agent":
            my_agent = AgentProfile.objects.get(user=self.notification_to)
            if my_agent:
                return "http://127.0.0.1:8000" + my_agent.profile_pic.url
            return ""

        if my_user.user_type == "Administrator":
            administrator = AdminProfile.objects.get(user=self.notification_to)
            if administrator:
                return "http://127.0.0.1:8000" + administrator.profile_pic.url
            return ""


class AgentsFloat(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requesting_agent")
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0, blank=True)
    paid = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.username

    def get_agents_phone(self):
        return self.agent.phone

    def get_agent_username(self):
        return self.agent.username

class PrivateChatId(models.Model):
    chat_id = models.CharField(max_length=400, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chat_id
class PrivateUserMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chatter2")
    private_chat_id = models.CharField(max_length=400, blank=True)
    message = models.TextField()
    read = models.BooleanField(default=False)
    isSender = models.BooleanField(default=False)
    isReceiver = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.private_chat_id

    def get_senders_username(self):
        return self.sender.username

    def get_receivers_username(self):
        return self.receiver.username

    def get_date(self):
        return humanize.naturaltime(self.timestamp)

    def save(self, *args, **kwargs):
        senders_username = self.sender.username
        receiver_username = self.receiver.username
        sender_receiver = str(senders_username) + str(receiver_username)
        receiver_sender = str(receiver_username) + str(senders_username)

        self.private_chat_id = sender_receiver

        super().save(*args, **kwargs)

class GroupMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_phone_number(self):
        return self.user.phone

    def get_date(self):
        return humanize.naturaltime(self.timestamp)


class AgentPreregistration(models.Model):
    name = models.CharField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    digital_address = models.CharField(max_length=15)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name