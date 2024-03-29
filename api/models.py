from datetime import datetime, timedelta
from decimal import Decimal

from django.conf import settings
from django.contrib.humanize.templatetags import humanize
from django.db import models
from django.utils import timezone

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
    ("POS", "POS"),
    ("Mobile App", "Mobile App"),
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
    ("Select deposit type", "Select deposit type"),
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

Join_Float_Status = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
)

NOTIFICATIONS_STATUS = (
    ("Read", "Read"),
    ("Not Read", "Not Read"),
)

NOTIFICATIONS_TRIGGERS = (
    ("Triggered", "Triggered"),
    ("Not Triggered", "Not Triggered"),
)

MTN_PAY_TO_TYPES = (
    ("Select pay to Type", "Select pay to Type"),
    ("Agent", "Agent"),
    ("Merchant", "Merchant"),
)

REQUEST_STATUS = (
    ("Approved", "Approved"),
    ("Pending", "Pending"),
)

AGENT_REQUEST_TYPE = (
    ("Network", "Network"),
    ("Bank", "Bank"),
    ("Cash", "Cash"),
)

PAYMENT_ACTIONS = (
    ("Select payment action", "Select payment action"),
    ("Not Closed", "Not Closed"),
    ("Close Payment", "Close Payment"),
)

MODE_OF_PAYMENT = (
    ("Select mode of payment", "Select mode of payment"),
    ("Bank Payment", "Bank Payment"),
    ("Mtn", "Mtn"),
    ("AirtelTigo", "AirtelTigo"),
    ("Vodafone", "Vodafone"),
    ("Momo pay", "Momo pay"),
    ("Agent to Agent", "Agent to Agent"),
    ("Cash left @", "Cash left @"),
    ("Own Accounts", "Own Accounts"),
    ("Company Accounts", "Company Accounts"),
)

PAYMENT_OFFICES = (
    ("Please select cash at location", "Please select cash at location"),
    ("Cash @ location", "Cash @ location"),
    ("DVLA", "DVLA"),
    ("HEAD OFFICE", "HEAD OFFICE"),
    ("KEJETIA", "KEJETIA"),
    ("ECOBANK", "ECOBANK"),
    ("PAN AFRICA", "PAN AFRICA"),
    ("MELCOM SANTASI", "MELCOM SANTASI"),
    ("MELCOM TANOSO", "MELCOM TANOSO"),
    ("MELCOM MANHYIA", "MELCOM MANHYIA"),
    ("MELCOM TAFO", "MELCOM TAFO"),
    ("MELCOM AHODWO", "MELCOM AHODWO"),
    ("MELCOM ADUM", "MELCOM ADUM"),
    ("MELCOM SUAME", "MELCOM SUAME"),
)

class Customer(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, unique=True, blank=True)
    customer_pic = models.ImageField(upload_to="customers_pics", default="default_user.png", blank=True)
    unique_code = models.CharField(max_length=500, default='',blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def get_customer_pic(self):
        if self.customer_pic:
            return "https://fnetagents.xyz" + self.customer_pic.url
        ""

    def __str__(self):
        return self.name

    def get_agents_phone(self):
        return self.agent.phone_number

    def get_agent_username(self):
        return self.agent.username

class CustomerAccounts(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100, blank=True, default="")
    account_number = models.CharField(max_length=16, blank=True)
    account_name = models.CharField(max_length=100, blank=True)
    bank = models.CharField(max_length=100, choices=BANKS, default="Access Bank")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer


    def get_agents_phone(self):
        return self.agent.phone_number

    def get_agent_username(self):
        return self.agent.username
class BankDeposit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agents_owner_bank_deposit")
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agent_requesting_bank")
    customer = models.CharField(max_length=100, blank=True, default="")
    depositor_name = models.CharField(max_length=30, blank=True, default="")
    depositor_number = models.CharField(max_length=30, blank=True, default="")
    bank = models.CharField(max_length=50, choices=BANKS, blank=True, default="")
    account_number = models.TextField(blank=True, max_length=17)
    account_name = models.CharField(max_length=100, blank=True, default="")
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    # total = models.DecimalField(decimal_places=2, max_digits=19, default=0.0)
    # d_200 = models.IntegerField(default=0, blank=True)
    # d_100 = models.IntegerField(default=0, blank=True)
    # d_50 = models.IntegerField(default=0, blank=True)
    # d_20 = models.IntegerField(default=0, blank=True)
    # d_10 = models.IntegerField(default=0, blank=True)
    # d_5 = models.IntegerField(default=0, blank=True)
    # d_2 = models.IntegerField(default=0, blank=True)
    # d_1 = models.IntegerField(default=0, blank=True)
    deposited_month = models.CharField(max_length=10, blank=True, default="")
    deposited_year = models.CharField(max_length=10, blank=True, default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # two_h_cedis_values = self.d_200 * 200
        # one_h_cedis_values = self.d_100 * 100
        # fifty_cedis_values = self.d_50 * 50
        # twenty_cedis_values = self.d_20 * 20
        # ten_cedis_values = self.d_10 * 10
        # five_cedis_values = self.d_5 * 5
        # two_cedis_values = self.d_2 * 2
        # one_cedi_values = self.d_1 * 1
        #
        # amount_total = Decimal(two_h_cedis_values) + Decimal(one_h_cedis_values) + Decimal(
        #     fifty_cedis_values) + Decimal(
        #     twenty_cedis_values) + Decimal(ten_cedis_values) + Decimal(five_cedis_values) + Decimal(
        #     two_cedis_values) + Decimal(one_cedi_values)
        # self.total = Decimal(amount_total)

        my_date = datetime.today()
        de_date = my_date.date()
        self.deposited_month = de_date.month
        self.deposited_year = de_date.year
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer

    def get_agents_phone(self):
        return self.agent.phone_number

    def get_agent_username(self):
        return self.agent.username

class MobileMoneyDeposit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agents_owner_momo_deposits")
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agent_requesting")
    customer = models.CharField(max_length=100, blank=True, default="")
    depositor_name = models.CharField(max_length=30, blank=True, default="")
    depositor_number = models.CharField(max_length=30, blank=True, default="")
    reference = models.CharField(max_length=100, blank=True, default="")
    network = models.CharField(max_length=20, choices=NETWORKS, blank=True, default="Select Network")
    type = models.CharField(max_length=20, blank=True, choices=MOBILE_MONEY_DEPOSIT_TYPE,default="")
    # total = models.DecimalField(decimal_places=2, max_digits=19, default=0.0)
    amount_sent = models.DecimalField(decimal_places=2, max_digits=19, default=0.0)
    cash_received = models.DecimalField(decimal_places=2, max_digits=19, default=0.0)
    # d_200 = models.IntegerField(default=0, blank=True)
    # d_100 = models.IntegerField(default=0, blank=True)
    # d_50 = models.IntegerField(default=0, blank=True)
    # d_20 = models.IntegerField(default=0, blank=True)
    # d_10 = models.IntegerField(default=0, blank=True)
    # d_5 = models.IntegerField(default=0, blank=True)
    # d_2 = models.IntegerField(default=0, blank=True)
    # d_1 = models.IntegerField(default=0, blank=True)
    d_date = models.DateField(auto_now_add=True)
    date_deposited = models.DateTimeField(auto_now_add=True)
    deposited_month = models.CharField(max_length=10, blank=True, default="")
    deposited_year = models.CharField(max_length=10, blank=True, default="")

    def save(self, *args, **kwargs):
        my_date = datetime.today()
        de_date = my_date.date()
        self.deposited_month = de_date.month
        self.deposited_year = de_date.year
        # two_h_cedis_values = self.d_200 * 200
        # one_h_cedis_values = self.d_100 * 100
        # fifty_cedis_values = self.d_50 * 50
        # twenty_cedis_values = self.d_20 * 20
        # ten_cedis_values = self.d_10 * 10
        # five_cedis_values = self.d_5 * 5
        # two_cedis_values = self.d_2 * 2
        # one_cedi_values = self.d_1 * 1

        # amount_total = Decimal(two_h_cedis_values) + Decimal(one_h_cedis_values) + Decimal(
        #     fifty_cedis_values) + Decimal(
        #     twenty_cedis_values) + Decimal(ten_cedis_values) + Decimal(five_cedis_values) + Decimal(
        #     two_cedis_values) + Decimal(one_cedi_values)
        # self.total = Decimal(amount_total)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Mobile money request made for {self.amount_sent} by {self.agent.username}"

    def get_agents_phone(self):
        return self.agent.phone_number

    def get_agent_username(self):
        return self.agent.username

class MobileMoneyWithdraw(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agents_owner_momo_withdrawals")
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100, blank=True, default="")
    network = models.CharField(max_length=20, choices=NETWORKS, blank=True, default="Select Network")
    cash_paid = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    amount_received = models.DecimalField(max_digits=19, decimal_places=2, blank=True,default=0.0)
    date_of_withdrawal = models.DateTimeField(auto_now_add=True)
    withdrawal_month = models.CharField(max_length=10, blank=True)
    withdrawal_year = models.CharField(max_length=10, blank=True)
    d_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        my_date = datetime.today()
        de_date = my_date.date()
        self.withdrawal_month = de_date.month
        self.withdrawal_year = de_date.year
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Withdrawal made for {self.cash_paid} by {self.agent.username}"

    def get_customer_name(self):
        return self.customer.name

    def get_customer_phone(self):
        return self.customer.phone

    def get_agents_phone(self):
        return self.agent.phone_number

    def get_agent_username(self):
        return self.agent.username

class BankWithdrawal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agents_owner_banks_withdrawals")
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100, blank=True, default="")
    bank = models.CharField(max_length=100, choices=BANKS, default="GT Bank")
    withdrawal_type = models.CharField(max_length=120, choices=BANK_REDRAW_ID_TYPES, default="Cheque")
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    # total = models.DecimalField(decimal_places=2, max_digits=19, default=0.0)
    # d_200 = models.IntegerField(default=0, blank=True)
    # d_100 = models.IntegerField(default=0, blank=True)
    # d_50 = models.IntegerField(default=0, blank=True)
    # d_20 = models.IntegerField(default=0, blank=True)
    # d_10 = models.IntegerField(default=0, blank=True)
    # d_5 = models.IntegerField(default=0, blank=True)
    # d_2 = models.IntegerField(default=0, blank=True)
    # d_1 = models.IntegerField(default=0, blank=True)
    date_of_withdrawal = models.DateTimeField(auto_now_add=True)
    withdrawal_month = models.CharField(max_length=10, blank=True, default="")
    withdrawal_year = models.CharField(max_length=10, blank=True, default="")

    def save(self, *args, **kwargs):
        # two_h_cedis_values = self.d_200 * 200
        # one_h_cedis_values = self.d_100 * 100
        # fifty_cedis_values = self.d_50 * 50
        # twenty_cedis_values = self.d_20 * 20
        # ten_cedis_values = self.d_10 * 10
        # five_cedis_values = self.d_5 * 5
        # two_cedis_values = self.d_2 * 2
        # one_cedi_values = self.d_1 * 1
        #
        # amount_total = Decimal(two_h_cedis_values) + Decimal(one_h_cedis_values) + Decimal(
        #     fifty_cedis_values) + Decimal(
        #     twenty_cedis_values) + Decimal(ten_cedis_values) + Decimal(five_cedis_values) + Decimal(
        #     two_cedis_values) + Decimal(one_cedi_values)
        # self.total = Decimal(amount_total)

        my_date = datetime.today()
        de_date = my_date.date()
        self.withdrawal_month = de_date.month
        self.withdrawal_year = de_date.year
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Withdrawal made for {self.amount} by {self.agent.username}"

    def get_agents_phone(self):
        return self.agent.phone_number

    def get_agent_username(self):
        return self.agent.username

class Reports(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_reports")
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
    customer = models.CharField(max_length=100, blank=True, default="")
    reason = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.customer

    def get_agents_username(self):
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

    # def notification_from_agent_username(self):
    #     return self.notification_from.username
    #
    # def notification_to_agent_username(self):
    #     return self.notification_to.username
    #
    # def get_notification_from_pic(self):
    #     my_user = User.objects.get(username=self.notification_from.username)
    #     if my_user.user_type == "Supervisor":
    #         my_supervisor = SupervisorProfile.objects.get(user=self.notification_from)
    #         if my_supervisor:
    #             return "http://127.0.0.1:8000" + my_supervisor.profile_pic.url
    #         return ""
    #
    #     if my_user.user_type == "Agent":
    #         my_agent = AgentProfile.objects.get(user=self.notification_from)
    #         if my_agent:
    #             return "http://127.0.0.1:8000" + my_agent.profile_pic.url
    #         return ""
    #
    #     if my_user.user_type == "Administrator":
    #         administrator = AdminProfile.objects.get(user=self.notification_from)
    #         if administrator:
    #             return "http://127.0.0.1:8000" + administrator.profile_pic.url
    #         return ""
    #
    # def get_notification_to_pic(self):
    #     my_user = User.objects.get(username=self.notification_to.username)
    #     if my_user.user_type == "Supervisor":
    #         my_supervisor = SupervisorProfile.objects.get(user=self.notification_to)
    #         if my_supervisor:
    #             return "http://127.0.0.1:8000" + my_supervisor.profile_pic.url
    #         return ""
    #
    #     if my_user.user_type == "Agent":
    #         my_agent = AgentProfile.objects.get(user=self.notification_to)
    #         if my_agent:
    #             return "http://127.0.0.1:8000" + my_agent.profile_pic.url
    #         return ""
    #
    #     if my_user.user_type == "Administrator":
    #         administrator = AdminProfile.objects.get(user=self.notification_to)
    #         if administrator:
    #             return "http://127.0.0.1:8000" + administrator.profile_pic.url
    #         return ""

class RegisteredForFloat(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="joining_agent")
    status = models.CharField(max_length=20,choices=Join_Float_Status, default="Pending")
    date_required = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.username

    def get_agent_username(self):
        return self.agent.username

    def get_agent_code(self):
        return self.agent.agent_unique_code

class Floats(models.Model):
    administrator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requesting_agent")
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0, blank=True)
    paid = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.username

    def get_agents_phone(self):
        return self.agent.phone_number

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
        return self.user.phone_number

    def get_date(self):
        return humanize.naturaltime(self.timestamp)

class AgentPreregistration(models.Model):
    name = models.CharField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    digital_address = models.CharField(max_length=15)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AuthenticateAgentPhone(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_id = models.CharField(max_length=255,unique=True)
    phone_model = models.CharField(max_length=55,unique=True)
    phone_brand = models.CharField(max_length=55,unique=True)
    finger_print = models.CharField(max_length=255,unique=True)
    phone_authenticated = models.BooleanField(default=False)
    date_authenticated = models.DateTimeField(auto_now_add=True)

    def get_agent_username(self):
        return self.agent.username

    def __str__(self):
        return self.agent.username

    def get_agent_unique_code(self):
        return self.agent.agent_unique_code

def one_month_trial(start_date):
    """Give a three-month trial to customers from a given start date."""

    # Convert start date string to datetime object
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')

    # Calculate trial end date as three months from start date
    trial_end_date = start_date_obj + timedelta(days=30)

    # Convert trial end date back to string format
    trial_end_date_str = trial_end_date.strftime('%Y-%m-%d')

    return trial_end_date_str
class FreeTrial(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=10, blank=True, default="")
    end_date = models.CharField(max_length=10, blank=True, default="")
    trial_started = models.BooleanField(default=True)
    trial_ended = models.BooleanField(default=False)
    date_started_trial = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.username

    def save(self, *args, **kwargs):
        my_date = datetime.today()
        self.start_date = my_date.date()
        self.end_date = one_month_trial(str(self.start_date))
        super().save(*args, **kwargs)

class MonthlyPayments(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=10, blank=True, default="")
    end_date = models.CharField(max_length=10, blank=True, default="")
    month_ended = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)


    def __Str__(self):
        return self.agent.username

    def save(self, *args, **kwargs):
        my_date = datetime.today()
        self.start_date = my_date.date()
        self.end_date = one_month_trial(str(self.start_date))
        super().save(*args, **kwargs)

class MtnPayTo(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100, blank=True, default="")
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    reference = models.CharField(max_length=100,default="",blank=True)
    depositor_number = models.CharField(max_length=100, default="", blank=True)
    pay_to_type = models.CharField(max_length=50,default="Agent",choices=MTN_PAY_TO_TYPES)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.customer

class SetUpMeeting(models.Model):
    administrator = models.ForeignKey(User, on_delete=models.CASCADE,related_name="admin",default=1)
    title = models.CharField(max_length=255)
    message = models.TextField()
    date_of_meeting = models.CharField(max_length=20)
    time_of_meeting = models.CharField(max_length=20)
    meeting_link = models.CharField(max_length=1500,default="")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Complains(models.Model):
    administrator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_complaining_to",default=1)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    complain = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_agent_username(self):
        return self.agent.username

    def get_agent_phone_number(self):
        return self.agent.phone_number

class HoldAccounts(models.Model):
    administrator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_views", default=1)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2,default=0.0)
    customer_number = models.CharField(max_length=20)
    merchant_id = models.CharField(max_length=20,default="")
    transaction_id = models.CharField(max_length=100,default="")
    reason = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.username

    def get_agent_username(self):
        return self.agent.username

    def get_agent_phone(self):
        return self.agent.phone_number
# new chat for agents and owners

class GroupOwnerMessage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.owner.username

    def get_username(self):
        return self.owner.username

    def get_phone_number(self):
        return self.owner.phone_number

    def get_date(self):
        return humanize.naturaltime(self.timestamp)

class GroupAgentsMessage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="owner_chatters")
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)


    def get_agent_username(self):
        return self.agent.username

    def __str__(self):
        return self.owner.username

    def get_username(self):
        return self.owner.username

    def get_phone_number(self):
        return self.user.phone_number

    def get_date(self):
        return humanize.naturaltime(self.timestamp)

# owner pay to
class OwnerMtnPayTo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_making_pay_to")
    agent_or_merchant = models.CharField(max_length=20, default="")
    amount = models.DecimalField(max_digits=19, decimal_places=2,default=0.0)
    reference = models.CharField(max_length=100,default="",blank=True)
    pay_to_type = models.CharField(max_length=50,default="Agent",choices=MTN_PAY_TO_TYPES)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent_or_merchant


class CheckAppVersion(models.Model):
    app_version = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"App version is currently {self.app_version}"


class CheckOwnerAppVersion(models.Model):
    app_version = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"App version is currently {self.app_version}"

class AgentAndOwnerAccounts(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, blank=True, default="")
    account_number = models.CharField(max_length=16, blank=True)
    account_name = models.CharField(max_length=100, blank=True)
    mtn_linked_number = models.CharField(max_length=100,default="")
    bank = models.CharField(max_length=100, choices=BANKS, default="GT Bank")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.username

    def get_agent_username(self):
        return self.agent.username

class AgentAccounts(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_with_agent_account')
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, blank=True, default="")
    account_number = models.CharField(max_length=16, blank=True)
    account_name = models.CharField(max_length=100, blank=True)
    mtn_linked_number = models.CharField(max_length=100,default="")
    bank = models.CharField(max_length=100, choices=BANKS, default="GT Bank")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.username

    def get_agent_username(self):
        return self.agent.username

class RequestFloat(models.Model):
    administrator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_owner',default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_requesting_for_float")
    float_request = models.CharField(max_length=255, default="Mtn")
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    approved = models.BooleanField(default=False)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username

    def get_owner_username(self):
        return self.owner.username

    def get_agent_username(self):
        return self.agent.username

class PayRequestedFloat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="owner_receiving_payments")
    agent = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_requesting_float")
    mode_of_payment1 = models.CharField(max_length=30, choices=MODE_OF_PAYMENT, blank=True,default="")
    mode_of_payment2 = models.CharField(max_length=30, choices=MODE_OF_PAYMENT, blank=True, default="")
    cash_at_location1 = models.CharField(max_length=30, choices=PAYMENT_OFFICES, blank=True, default="")
    cash_at_location2 = models.CharField(max_length=30, choices=PAYMENT_OFFICES, blank=True, default="")
    bank1 = models.CharField(max_length=50, choices=BANKS, blank=True, default="")
    bank2 = models.CharField(max_length=50, choices=BANKS, blank=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0, blank=True)
    amount1 = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    amount2 = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    transaction_id1 = models.CharField(max_length=30, blank=True, default="")
    transaction_id2 = models.CharField(max_length=30, blank=True, default="")
    payment_action = models.CharField(max_length=50, choices=PAYMENT_ACTIONS, default="Close Payment")
    payment_status = models.CharField(max_length=20, choices=REQUEST_STATUS, default="Pending")
    payment_month = models.CharField(max_length=10, blank=True, default="")
    payment_year = models.CharField(max_length=10, blank=True, default="")
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)

    def get_agent_username(self):
        return self.agent.username
    def __str__(self):
        return self.agent.username

    def save(self, *args, **kwargs):
        my_date = datetime.today()
        de_date = my_date.date()
        self.payment_month = de_date.month
        self.payment_year = de_date.year

        amount_total = Decimal(self.amount1) + Decimal(self.amount2)
        self.amount = Decimal(amount_total)
        super().save(*args, **kwargs)
