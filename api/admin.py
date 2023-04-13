from django.contrib import admin
from .models import Customer, CustomerAccounts, BankDeposit, MobileMoneyDeposit, MobileMoneyWithdraw, BankWithdrawal, PaymentForReBalancing, Reports, AddToBlockList, Fraud, AgentReBalancing, AuthenticatedPhoneAddress, Notifications, AgentAccounts, AgentsFloat

admin.site.register(Customer)
admin.site.register(CustomerAccounts)
admin.site.register(BankDeposit)
admin.site.register(MobileMoneyDeposit)
admin.site.register(MobileMoneyWithdraw)
admin.site.register(BankWithdrawal)
admin.site.register(PaymentForReBalancing)
admin.site.register(AddToBlockList)
admin.site.register(Fraud)
admin.site.register(AgentReBalancing)
admin.site.register(AuthenticatedPhoneAddress)
admin.site.register(Notifications)
admin.site.register(AgentAccounts)
admin.site.register(AgentsFloat)
admin.site.register(Reports)
