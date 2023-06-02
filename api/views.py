from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from datetime import datetime
from .process_mail import send_my_mail
from django.conf import settings
from users.models import User
from users.serializers import UsersSerializer
from .models import (Customer, CustomerAccounts, BankDeposit, MobileMoneyDeposit, MobileMoneyWithdraw, BankWithdrawal, \
                     PaymentForReBalancing, Reports, AddToBlockList, Fraud, AgentReBalancing, Notifications, AgentAccounts, Floats, \
                     GroupMessage, PrivateUserMessage, AgentPreregistration, RegisteredForFloat, AgentAccountsBalanceStarted, AgentAccountsBalanceClosed, FreeTrial, MonthlyPayments, AuthenticateAgentPhone, MtnPayTo, AgentRequest, AgentRequestLimit, SetUpMeeting, Complains, HoldAccounts, AgentRequestPayment, GroupOwnerMessage,GroupAgentsMessage)
from .serializers import (CustomerSerializer, CustomerAccountsSerializer, BankDepositSerializer, MomoDepositSerializer, \
                          MomoWithdrawalSerializer, BankWithdrawalSerializer, PaymentForReBalancingSerializer,
                          ReportSerializer, \
                          AddToBlockListSerializer, NotificationSerializer, AgentReBalancingSerializer,
                          AgentAccountsSerializer, \
                          AgentsFloatSerializer, FraudSerializer, GroupMessageSerializer, PrivateUserMessageSerializer,
                          AgentPreregistrationSerializer, RegisteredForFloatSerializer,AgentAccountsBalanceStartedSerializer, AgentAccountsBalanceClosedSerializer,AuthenticateAgentPhoneSerializer,FreeTrialSerializer,MonthlyPaymentsSerializer,MtnPayToSerializer,AgentRequestLimitSerializer,AgentRequestSerializer,SetUpMeetingSerializer,ComplainsSerializer,HoldAccountsSerializer,AddedToApprovedPaymentSerializer,AddedToApprovedRequestSerializer,AgentRequestPaymentSerializer,AddedToApprovedReBalancingSerializer,GroupAgentsMessageSerializer,GroupOwnerMessageSerializer)


# float joining
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_to_join_float(request):
    serializer = RegisteredForFloatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_request_to_join_float(request):
    agents_requesting = RegisteredForFloat.objects.all().order_by('-date_requested')
    serializer = RegisteredForFloatSerializer(agents_requesting, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_request_to_join_float(request):
    agents_requesting = RegisteredForFloat.objects.filter(agent=request.user)
    serializer = RegisteredForFloatSerializer(agents_requesting, many=True)
    return Response(serializer.data)

# agent pre registration
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_agent_pre_reg(request):
    serializer = AgentPreregistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_agents_pre_registrations(request):
    agents_requesting = AgentPreregistration.objects.all().order_by('-date_registered')
    serializer = AgentPreregistrationSerializer(agents_requesting, many=True)
    return Response(serializer.data)
# private and public messages
# group message post and get request
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def send_group_message(request):
    serializer = GroupMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_group_message(request):
    messages = GroupMessage.objects.all().order_by('timestamp')
    serializer = GroupMessageSerializer(messages, many=True)
    return Response(serializer.data)


# private messages
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def send_private_message(request):
    serializer = PrivateUserMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_private_message(request, user1, user2):
    all_messages = []
    messages1 = PrivateUserMessage.objects.filter(sender=user1, receiver=user2).order_by('-timestamp')
    messages2 = PrivateUserMessage.objects.filter(sender=user2, receiver=user1).order_by('-timestamp')
    for i in messages1:
        all_messages.append(i)

    for m in messages2:
        all_messages.append(m)
    serializer = PrivateUserMessageSerializer(all_messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def private_message_detail(request, user1, user2):
    message = PrivateUserMessage.objects.get(sender=user1, receiver=user2)
    if message:
        message.read = True
        message.save()
    serializer = PrivateUserMessageSerializer(message, many=False)
    return Response(serializer.data)


# for customers
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def register_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchCustomers(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Customer.objects.all().order_by('-date_created')
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'phone']

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def customer_details(request, pk):
    customer = Customer.objects.get(pk=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def customer_details_by_phone(request, phone):
    customer = Customer.objects.filter(phone=phone)
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def customer_details_by_name(request, name):
    customer = Customer.objects.filter(name=name)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_customers(request, username):
    user = get_object_or_404(User, username=username)
    u_customers = Customer.objects.filter(agent=user).order_by('-date_created')
    serializer = CustomerSerializer(u_customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_customers(request):
    customers = Customer.objects.filter(agent=request.user).order_by('-date_created')
    serializer = CustomerSerializer(customers,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_customers(request):
    customers = Customer.objects.all().order_by('-date_created')
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_customer(request,pk):
    customer = get_object_or_404(Customer,pk=pk)
    serializer = CustomerSerializer(customer,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def customer_delete(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        customer.delete()
    except Customer.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)



# register customers accounts
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def register_customer_accounts(request):
    serializer = CustomerAccountsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchCustomersAccounts(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = CustomerAccounts.objects.all().order_by('-date_added')
    serializer_class = CustomerAccountsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['account_name','account_number']

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def customer_accounts_details(request, pk):
    customer = CustomerAccounts.objects.get(pk=pk)
    serializer = CustomerAccountsSerializer(customer, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def customer_accounts_details_by_account_number(request, account_number):
    customer = CustomerAccounts.objects.filter(account_number=account_number)
    serializer = CustomerAccountsSerializer(customer, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def customer_account_details_by_account_name(request, account_name):
    customer = CustomerAccounts.objects.filter(account_name=account_name)
    serializer = CustomerAccountsSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_customer_accounts(request,pk):
    customer_account = get_object_or_404(CustomerAccounts,pk=pk)
    serializer = CustomerAccountsSerializer(customer_account,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def customer_account_delete(request, pk):
    try:
        customer_account = CustomerAccounts.objects.get(pk=pk)
        customer_account.delete()
    except CustomerAccounts.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

# bank deposits
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_bank_deposit(request):
    serializer = BankDepositSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchBankDeposit(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BankDeposit.objects.all().order_by('-date_added')
    serializer_class = BankDepositSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['account_number', 'account_name','date_added']

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def bank_details(request, pk):
    bank = BankDeposit.objects.get(pk=pk)
    serializer = BankDepositSerializer(bank, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_bank_deposits(request, username):
    user = get_object_or_404(User, username=username)
    agents_bank_deposits = BankDeposit.objects.filter(agent=user).order_by('-date_added')
    serializer = BankDepositSerializer(agents_bank_deposits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_bank_deposits(request):
    deposits = BankDeposit.objects.all().order_by('-date_added')
    serializer = BankDepositSerializer(deposits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_bank_deposits(request):
    deposits = BankDeposit.objects.filter(agent=request.user).order_by('-date_added')
    serializer = BankDepositSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_customer_bank_deposits(request,pk):
    customer = get_object_or_404(Customer,pk=pk)
    customers_deposits = BankDeposit.objects.filter(customer=customer)
    serializer = BankDepositSerializer(customers_deposits,many=True)
    return Response(serializer.dat)


# mobile money deposit
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_momo_deposit(request):
    serializer = MomoDepositSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchMomoDeposit(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MobileMoneyDeposit.objects.all().order_by('-date_deposited')
    serializer_class = MomoDepositSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['network', 'date_deposited']

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def momo_deposit_details(request, pk):
    momo = MobileMoneyDeposit.objects.get(pk=pk)
    serializer = MomoDepositSerializer(momo, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_momo_deposits(request, username):
    user = get_object_or_404(User, username=username)
    agents_momo_deposits = MobileMoneyDeposit.objects.filter(agent=user).order_by('-date_deposited')
    serializer = MomoDepositSerializer(agents_momo_deposits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_momo_deposits(request):
    deposits = MobileMoneyDeposit.objects.all().order_by('-date_deposited')
    serializer = MomoDepositSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_momo_deposits(request):
    deposits = MobileMoneyDeposit.objects.filter(agent=request.user).order_by('-date_deposited')
    serializer = MomoDepositSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_customer_momo_deposits(request,pk):
    customer = get_object_or_404(Customer,pk=pk)
    customers_deposits = MobileMoneyDeposit.objects.filter(customer=customer)
    serializer = MomoDepositSerializer(customers_deposits,many=True)
    return Response(serializer.dat)

# momo withdrawal
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_momo_withdrawal(request):
    serializer = MomoWithdrawalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchMomoWithdrawal(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MobileMoneyWithdraw.objects.all().order_by('-date_of_withdrawal')
    serializer_class = MomoWithdrawalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['network', 'date_of_withdrawal']

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def momo_withdrawal_details(request, pk):
    momo = MobileMoneyWithdraw.objects.get(pk=pk)
    serializer = MomoWithdrawalSerializer(momo, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_momo_withdrawals(request, username):
    user = get_object_or_404(User, username=username)
    agents_momo_deposits = MobileMoneyWithdraw.objects.filter(agent=user).order_by('-date_of_withdrawal')
    serializer = MomoWithdrawalSerializer(agents_momo_deposits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_momo_withdraws(request):
    withdrawals = MobileMoneyWithdraw.objects.all().order_by('-date_of_withdrawal')
    serializer = MomoWithdrawalSerializer(withdrawals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_momo_withdraws(request):
    deposits = MobileMoneyWithdraw.objects.filter(agent=request.user).order_by('-date_of_withdrawal')
    serializer = MomoWithdrawalSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_customer_momo_withdrawals(request,pk):
    customer = get_object_or_404(Customer,pk=pk)
    customers_withdrawals = MobileMoneyWithdraw.objects.filter(customer=customer)
    serializer = MomoWithdrawalSerializer(customers_withdrawals,many=True)
    return Response(serializer.dat)


# bank withdrawal
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_bank_withdrawal(request):
    serializer = BankWithdrawalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchBankWithdrawal(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BankWithdrawal.objects.all().order_by('-date_of_withdrawal')
    serializer_class = BankWithdrawalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['bank','date_of_withdrawal']

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def bank_withdrawal_details(request, pk):
    bank = BankWithdrawal.objects.get(pk=pk)
    serializer = BankWithdrawalSerializer(bank, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_bank_withdrawals(request, username):
    user = get_object_or_404(User, username=username)
    agents_bank_withdrawals = BankWithdrawal.objects.filter(agent=user).order_by('-date_of_withdrawal')
    serializer = BankWithdrawalSerializer(agents_bank_withdrawals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_bank_withdrawals(request):
    withdrawals = BankWithdrawal.objects.all().order_by('-date_of_withdrawal')
    serializer = BankWithdrawalSerializer(withdrawals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_bank_withdrawals(request):
    withdrawals = BankWithdrawal.objects.filter(agent=request.user).order_by('-date_of_withdrawal')
    serializer = BankWithdrawalSerializer(withdrawals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_customer_bank_withdrawals(request,pk):
    customer = get_object_or_404(Customer,pk=pk)
    customers_withdrawals = BankWithdrawal.objects.filter(customer=customer)
    serializer = BankWithdrawalSerializer(customers_withdrawals,many=True)
    return Response(serializer.dat)


# reports
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_report(request):
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def report_detail(request, pk):
    report = Reports.objects.get(pk=pk)
    serializer = ReportSerializer(report, many=False)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def delete_report(request, id):
    try:
        report = get_object_or_404(Reports, id=id)
        report.delete()
    except Reports.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_reports(request, username):
    user = get_object_or_404(User, username=username)
    reports = Reports.objects.filter(user=user).order_by('-date_reported')
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_reports(request):
    reports = Reports.objects.all().order_by('-date_reported')
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_reports_today(request):
    my_date = datetime.today()
    for_today = my_date.date()
    reports = Reports.objects.filter(date_reported=for_today).order_by('date_reported')
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_reports(request):
    reports = Reports.objects.filter(user=request.user).order_by('-date_reported')
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)

# add to blocked list
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_blocked_lists(request):
    serializer = AddToBlockListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_blocked(request):
    blocked_lists = AddToBlockList.objects.all().order_by('-date_blocked')
    serializer = AddToBlockListSerializer(blocked_lists, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def remove_from_blocked(request, id):
    try:
        user_blocked = get_object_or_404(AddToBlockList, id=id)
        user_blocked.delete()
    except AddToBlockList.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

# fraud
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_fraud_lists(request):
    serializer = FraudSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def fraud_detail(request, pk):
    fraud = Fraud.objects.get(pk=pk)
    serializer = FraudSerializer(fraud, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_fraudsters(request):
    fraud_lists = Fraud.objects.all().order_by('-date_added')
    serializer = FraudSerializer(fraud_lists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_fraud_lists(request):
    fraud = Fraud.objects.filter(agent=request.user).order_by('-date_added')
    serializer = FraudSerializer(fraud, many=True)
    return Response(serializer.data)

class SearchFraudsters(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Fraud.objects.all().order_by('-date_added')
    serializer_class = FraudSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date_added']


# payment for balancing
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_payment_for_re_balancing(request):
    serializer = PaymentForReBalancingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchPaymentForReBalancing(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PaymentForReBalancing.objects.all().order_by('-date_created')
    serializer_class = PaymentForReBalancingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date_created']

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def payment_details(request, pk):
    payment = PaymentForReBalancing.objects.get(pk=pk)
    serializer = PaymentForReBalancingSerializer(payment, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_payments(request, username):
    user = get_object_or_404(User, username=username)
    payments = PaymentForReBalancing.objects.filter(agent=user).order_by('-date_created')
    serializer = PaymentForReBalancingSerializer(payments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_payments(request):
    payments = PaymentForReBalancing.objects.all().order_by('-date_created')
    serializer = PaymentForReBalancingSerializer(payments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_payments(request):
    payments = PaymentForReBalancing.objects.filter(agent=request.user).order_by('-date_created')
    serializer = PaymentForReBalancingSerializer(payments, many=True)
    return Response(serializer.data)

# agent rebalancing
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_for_re_balancing(request):
    serializer = AgentReBalancingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchAgentsForReBalancing(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = AgentReBalancing.objects.all().order_by('-date_requested')
    serializer_class = AgentReBalancingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['bank','account_number','account_name','date_requested']

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def re_balancing_details(request, pk):
    balancing = AgentReBalancing.objects.get(pk=pk)
    serializer = AgentReBalancingSerializer(balancing, many=False)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def delete_agent_rebalancing(request, id):
    try:
        rebalance = get_object_or_404(AgentReBalancing, id=id)
        rebalance.delete()
    except AgentReBalancingSerializer.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_re_balancing_requests(request, username):
    user = get_object_or_404(User, username=username)
    balancing = AgentReBalancing.objects.filter(agent=user).order_by('-date_requested')
    serializer = AgentReBalancingSerializer(balancing, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_unapproved_re_balancing_requests(request):
    balancing = AgentReBalancing.objects.filter(request_approved="Pending").order_by("-date_requested")
    serializer = AgentReBalancingSerializer(balancing,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_re_balancing(request):
    balancing = AgentReBalancing.objects.all().order_by('-date_requested')
    serializer = AgentReBalancingSerializer(balancing, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_re_balancing_requests(request):
    balancing = AgentReBalancing.objects.filter(agent=request.user).order_by('-date_requested')
    serializer = AgentReBalancingSerializer(balancing, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_agent_rebalancing(request,pk):
    a_request = get_object_or_404(AgentReBalancing, pk=pk)
    serializer = AgentReBalancingSerializer(a_request,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# agents accounts registration
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def register_agents_accounts(request):
    serializer = AgentAccountsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchAgentsAccounts(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AgentAccounts.objects.all().order_by('-date_added')
    serializer_class = AgentAccountsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['account_name','account_number','bank','date_added']

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def agent_accounts_details(request, pk):
    agent = AgentAccounts.objects.get(pk=pk)
    serializer = AgentAccountsSerializer(agent, many=False)
    return Response(serializer.data)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agent_accounts_by_username(request, username):
    user = get_object_or_404(User, username=username)
    agent = AgentAccounts.objects.filter(agent=user).order_by('-date_added')
    serializer = AgentAccountsSerializer(agent, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def agent_accounts_details_by_account_number(request, account_number):
    agent = AgentAccounts.objects.filter(account_number=account_number)
    serializer = AgentAccountsSerializer(agent, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def agent_account_details_by_account_name(request, account_name):
    agent = AgentAccounts.objects.filter(account_name=account_name)
    serializer = AgentAccountsSerializer(agent, many=False)
    return Response(serializer.data)


@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_agents_accounts(request,pk):
    agent_account = get_object_or_404(AgentAccounts,pk=pk)
    serializer = AgentAccountsSerializer(agent_account,data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def agent_account_delete(request, pk):
    try:
        agent_account = AgentAccounts.objects.get(pk=pk)
        agent_account.delete()
    except AgentAccounts.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_accounts(request):
    accounts = AgentAccounts.objects.filter(agent=request.user).order_by('-date_added')
    serializer = AgentAccountsSerializer(accounts,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_agents_accounts(request):
    accounts = AgentAccounts.objects.filter(owner=request.user).order_by('-date_added')
    serializer = AgentAccountsSerializer(accounts,many=True)
    return Response(serializer.data)

# notifications
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).order_by('date_created')[:50]
    serializer = NotificationSerializer(notifications,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_unread_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).filter(read="Not Read").order_by('date_created')
    serializer = NotificationSerializer(notifications,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def read_notification(request):
    notifications = Notifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by('-date_created')
    for i in notifications:
        i.read = "Read"
        i.save()

    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def un_trigger_notification(request, id):
    notification = get_object_or_404(Notifications, id=id)
    serializer = NotificationSerializer(notification, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_triggered_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).filter(
        notification_trigger="Triggered").filter(
        read="Not Read").order_by('-date_created')[:50]
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)


# agents float
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_float(request):
    serializer = AgentsFloatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchAgentsFloats(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Floats.objects.all().order_by('-date_added')
    serializer_class = AgentsFloatSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date_added']

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def float_details(request, pk):
    agent_float = Floats.objects.get(pk=pk)
    serializer = AgentsFloatSerializer(agent_float, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_float_requests(request, username):
    user = get_object_or_404(User, username=username)
    agent_float = Floats.objects.filter(agent=user).order_by('-date_added')
    serializer = AgentsFloatSerializer(agent_float, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_floats(request):
    floats = Floats.objects.all().order_by('-date_added')
    serializer = AgentsFloatSerializer(floats, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_float_requests(request):
    floats = Floats.objects.filter(agent=request.user).order_by('-date_added')
    serializer = AgentsFloatSerializer(floats, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def get_all_my_agents(request):
#     agents = User.objects.filter(supervisor=request.user)
#     serializer = UsersSerializer(agents, many=True)
#     return Response(serializer.data)

# new functions for customer accounts
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_customer_account(request, customer):
    c_detail = CustomerAccounts.objects.filter(customer=customer).order_by('-date_added')
    serializer = CustomerAccountsSerializer(c_detail, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_customer_accounts_by_bank(request, customer_phone, bank):
    customer_accounts = CustomerAccounts.objects.filter(customer=customer_phone).filter(bank=bank).order_by('-date_added')
    serializer = CustomerAccountsSerializer(customer_accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_customer_by_phone(request, customer):
    customer = Customer.objects.filter(customer=customer)
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)


# agents accounts added and closed
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_balance_to_start(request):
    serializer = AgentAccountsBalanceStartedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_balance_to_start(request,pk):
    account_balance = get_object_or_404(AgentAccountsBalanceStarted,pk=pk)
    serializer = AgentAccountsBalanceStartedSerializer(account_balance,data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_account_balance_started(request):
    my_account_balance = AgentAccountsBalanceStarted.objects.filter(agent=request.user).order_by('-date_posted')
    serializer = AgentAccountsBalanceStartedSerializer(my_account_balance, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_account_balance_started_today(request):
    my_date = datetime.today()
    for_today = my_date.date()
    my_account_balance = AgentAccountsBalanceStarted.objects.filter(agent=request.user).filter(date_posted=for_today).order_by('date_posted')
    serializer = AgentAccountsBalanceStartedSerializer(my_account_balance, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def close_balance(request):
    serializer = AgentAccountsBalanceClosedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_account_balance_closed(request):
    my_account_balance = AgentAccountsBalanceClosed.objects.filter(agent=request.user)
    serializer = AgentAccountsBalanceClosedSerializer(my_account_balance, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_account_balance_closed_today(request):
    my_date = datetime.today()
    for_today = my_date.date()
    my_account_balance = AgentAccountsBalanceClosed.objects.filter(agent=request.user).filter(date_closed=for_today)
    serializer = AgentAccountsBalanceClosedSerializer(my_account_balance, many=True)
    return Response(serializer.data)


# authenticate agent phone
@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def authenticate_agent_phone(request):
    serializer = AuthenticateAgentPhoneSerializer(data=request.data)
    if serializer.is_valid():
        if not AuthenticateAgentPhone.objects.filter(agent=request.user).exists():
            serializer.save(agent=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_auth_phones(request):
    auth_phones = AuthenticateAgentPhone.objects.all().order_by("-date_authenticated")
    serializer = AuthenticateAgentPhoneSerializer(auth_phones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_auth_phone_agent_by_phone_id(request,phone_id):
    agent_auth_phone = AuthenticateAgentPhone.objects.filter(phone_id=phone_id)
    serializer = AuthenticateAgentPhoneSerializer(agent_auth_phone, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_auth_phone_by_username(request, username):
    user = get_object_or_404(User, username=username)
    agent_auth_phone = AuthenticateAgentPhone.objects.filter(agent=user).order_by('-date_authenticated')
    serializer = AuthenticateAgentPhoneSerializer(agent_auth_phone, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def delete_auth_phone(request, id):
    try:
        agent_phone = get_object_or_404(AuthenticateAgentPhone, id=id)
        agent_phone.delete()
    except AuthenticateAgentPhone.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

# free trial
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def start_free_trial(request):
    serializer = FreeTrialSerializer(data=request.data)
    if serializer.is_valid():
        if not FreeTrial.objects.filter(agent=request.user).exists():
            serializer.save(agent=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_free_trial(request,pk):
    trial = get_object_or_404(FreeTrial, pk=pk)
    serializer = FreeTrialSerializer(trial,data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_free_trial(request):
    my_details = FreeTrial.objects.filter(agent=request.user)
    serializer = FreeTrialSerializer(my_details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_free_trials(request):
    free_trials = FreeTrial.objects.all().order_by('-date_started_trial')
    serializer = FreeTrialSerializer(free_trials, many=True)
    return Response(serializer.data)

# monthly payments
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def make_monthly_payment(request):
    serializer = MonthlyPaymentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_monthly_payment_status(request):
    my_payments = MonthlyPayments.objects.filter(agent=request.user)
    serializer = MonthlyPaymentsSerializer(my_payments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_monthly_payment_status(request):
    monthly_payments = MonthlyPayments.objects.all().order_by('-date_added')
    serializer = FreeTrialSerializer(monthly_payments, many=True)
    return Response(serializer.data)

# activating trial and monthly ended payment
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def end_trial(request):
    my_date = datetime.today()
    for_today = my_date.date()
    free_trials = FreeTrial.objects.all().order_by('-date_started_trial')
    for i in free_trials:
        if i.end_date == for_today:
            i.trial_ended = True
            i.save()
    serializer = FreeTrialSerializer(free_trials, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def end_monthly_payment(request):
    my_date = datetime.today()
    for_today = my_date.date()
    monthly_payments = MonthlyPayments.objects.all().order_by('-date_added')
    for i in monthly_payments:
        if i.end_date == for_today:
            i.month_ended = True
            i.save()
    serializer = MonthlyPaymentsSerializer(monthly_payments, many=True)
    return Response(serializer.data)

# mtn pay to
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_pay_to(request):
    serializer = MtnPayToSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_pay_to(request):
    pay_tos = MtnPayTo.objects.all().order_by('-date_added')
    serializer = MtnPayToSerializer(pay_tos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_pay_to(request):
    pay_tos = MtnPayTo.objects.filter(agent=request.user).order_by('-date_added')
    serializer = MtnPayToSerializer(pay_tos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_agents(request,owner):
    agents = User.objects.filter(owner=owner)
    serializer = UsersSerializer(agents, many=True)
    return Response(serializer.data)


# getting individual agents transactions
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_customers(request, username):
    user = get_object_or_404(User, username=username)
    customers = Customer.objects.filter(agent=user).order_by('-date_created')
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_bank_deposits(request, username):
    user = get_object_or_404(User, username=username)
    deposits = BankDeposit.objects.filter(agent=user).order_by('-date_added')
    serializer = BankDepositSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_bank_withdrawals(request, username):
    user = get_object_or_404(User, username=username)
    withdrawals = BankWithdrawal.objects.filter(agent=user).order_by('-date_of_withdrawal')
    serializer = BankWithdrawalSerializer(withdrawals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_momo_deposits(request, username):
    user = get_object_or_404(User, username=username)
    deposits = MobileMoneyDeposit.objects.filter(agent=user).order_by('-date_deposited')
    serializer = MomoDepositSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_momo_withdrawals(request, username):
    user = get_object_or_404(User, username=username)
    withdrawals = MobileMoneyWithdraw.objects.filter(agent=user).order_by('-date_of_withdrawal')
    serializer = MomoWithdrawalSerializer(withdrawals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_momo_pay_to(request, username):
    user = get_object_or_404(User, username=username)
    pay_tos = MtnPayTo.objects.filter(agent=user).order_by('-date_added')
    serializer = MtnPayToSerializer(pay_tos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_reports(request, username):
    user = get_object_or_404(User, username=username)
    reports = Reports.objects.filter(agent=user).order_by('-date_reported')
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)

# agent request
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def agent_request_from_owner(request):
    serializer = AgentRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_agents_requests(request):
    agent_requests = AgentRequest.objects.filter(owner=request.user).order_by("-date_requested")
    serializer = AgentRequestSerializer(agent_requests,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_requests(request):
    agent_requests = AgentRequest.objects.filter(agent=request.user).order_by("-date_requested")
    serializer = AgentRequestSerializer(agent_requests,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_requests_today(request):
    my_date = datetime.today()
    for_today = my_date.date()
    agent_requests = AgentRequest.objects.filter(agent=request.user).filter(date_requested=for_today).order_by('date_requested')
    serializer = AgentRequestSerializer(agent_requests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def request_detail(request,pk):
    detail_request = get_object_or_404(AgentRequest,pk=pk)
    serializer = AgentRequestSerializer(detail_request,many=False)
    return Response(serializer.data)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_agent_request(request,pk):
    a_request = get_object_or_404(AgentRequest, pk=pk)
    serializer = AgentRequestSerializer(a_request,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def delete_agent_request(request, id):
    try:
        agent_request = get_object_or_404(AgentRequest, id=id)
        agent_request.delete()
    except AgentRequest.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_unapproved_requests(request):
    all_requests = AgentRequest.objects.filter(request_approved="Pending").order_by("-date_requested")
    serializer = AgentRequestSerializer(all_requests,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_unpaid_requests(request):
    all_requests = AgentRequest.objects.filter(request_paid="Pending").order_by("-date_requested")
    serializer = AgentRequestSerializer(all_requests,many=True)
    return Response(serializer.data)

# agent request limit
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_agent_request_limit(request):
    serializer = AgentRequestLimitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_agent_request_limit(request,pk):
    a_request = get_object_or_404(AgentRequestLimit, pk=pk)
    serializer = AgentRequestLimitSerializer(a_request,data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_agents_request_limits(request):
    agents = AgentRequestLimit.objects.filter(owner=request.user).order_by("-date_added")
    serializer = AgentRequestLimitSerializer(agents,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_request_limit(request):
    agents = AgentRequestLimit.objects.filter(agent=request.user).order_by("-date_added")
    serializer = AgentRequestLimitSerializer(agents,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def admin_set_up_meeting(request):
    serializer = SetUpMeetingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(administrator=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_meetings(request):
    meetings = SetUpMeeting.objects.all().order_by("-date_created")
    serializer = SetUpMeetingSerializer(meetings,many=True)
    return Response(serializer.data)


# complains
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_complain(request):
    serializer = ComplainsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_complains(request):
    complains = Complains.objects.all().order_by("-date_added")
    serializer = ComplainsSerializer(complains,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_complains(request):
    complains = Complains.objects.filter(agent=request.user).order_by("-date_added")
    serializer = ComplainsSerializer(complains, many=True)
    return Response(serializer.data)


# request to hold account
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_to_hold_account(request):
    serializer = HoldAccountsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_request_to_hold_account(request):
    my_requests = HoldAccounts.objects.all().order_by("-date_added")
    serializer = HoldAccountsSerializer(my_requests,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_request_to_hold_account(request):
    my_requests = HoldAccounts.objects.filter(agent=request.user).order_by("-date_added")
    serializer = HoldAccountsSerializer(my_requests, many=True)
    return Response(serializer.data)


# agent request by username
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_request_username(request, username):
    user = get_object_or_404(User, username=username)
    all_requests = AgentRequest.objects.filter(agent=user).order_by('-date_requested')
    serializer = AgentRequestSerializer(all_requests, many=True)
    return Response(serializer.data)

# agent make payment request
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def make_request_payment(request):
    serializer = AgentRequestPaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_agents_payment_requests(request):
    payment_requests = AgentRequestPayment.objects.filter(owner=request.user).order_by("-date_requested")
    serializer = AgentRequestPaymentSerializer(payment_requests,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def payment_request_detail(request,pk):
    payment_request = get_object_or_404(AgentRequestPayment,pk=pk)
    serializer = AgentRequestPaymentSerializer(payment_request,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_payment_requests(request):
    payment_requests = AgentRequestPayment.objects.filter(agent=request.user).order_by("-date_requested")
    serializer = AgentRequestPaymentSerializer(payment_requests,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_payment_requests_today(request):
    my_date = datetime.today()
    for_today = my_date.date()
    agent_requests = AgentRequestPayment.objects.filter(agent=request.user).filter(date_requested=for_today).order_by('date_requested')
    serializer = AgentRequestPaymentSerializer(agent_requests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_payment_request_username(request, username):
    user = get_object_or_404(User, username=username)
    all_requests = AgentRequestPayment.objects.filter(agent=user).order_by('-date_requested')
    serializer = AgentRequestPaymentSerializer(all_requests, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_agent_payment_request(request,pk):
    a_request = get_object_or_404(AgentRequestPayment, pk=pk)
    serializer = AgentRequestPaymentSerializer(a_request,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def delete_agent_payment_request(request, id):
    try:
        payment_request = get_object_or_404(AgentRequestPayment, id=id)
        payment_request.delete()
    except AgentRequestPayment.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_unapproved_payment_requests(request):
    payment_requests = AgentRequestPayment.objects.filter(payment_approved="Pending").order_by("-date_requested")
    serializer = AgentRequestPaymentSerializer(payment_requests,many=True)
    return Response(serializer.data)


# approvals
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_approve_request_payment(request):
    serializer = AddedToApprovedPaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_approve_request(request):
    serializer = AddedToApprovedRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)\

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_approve_request_rebalancing(request):
    serializer = AddedToApprovedReBalancingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# owners and agents messages
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def send_owners_group_message(request):
    serializer = GroupOwnerMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_owners_group_messages(request):
    messages = GroupOwnerMessage.objects.all().order_by('timestamp')
    serializer = GroupOwnerMessageSerializer(messages,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def send_agents_group_message(request):
    serializer = GroupAgentsMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_group_messages(request,owner):
    messages = GroupAgentsMessage.objects.filter(owner=owner).order_by('timestamp')
    serializer = GroupAgentsMessageSerializer(messages,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def send_otp(request,otp,email,username):
    send_my_mail(f"Hi from Easy Agent", settings.EMAIL_HOST_USER, email, {"name": username,"OTP": otp},"email_templates/sendotp.html")
    return Response()



