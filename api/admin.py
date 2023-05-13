from django.contrib import admin
from .models import Customer, CustomerAccounts, BankDeposit, MobileMoneyDeposit, MobileMoneyWithdraw, BankWithdrawal, PaymentForReBalancing, Reports, AddToBlockList, Fraud, AgentReBalancing, Notifications, AgentAccounts, AgentsFloat,PrivateChatId,PrivateUserMessage,GroupMessage,AgentPreregistration,RegisteredForFloat, AgentAccountsBalanceStarted, AgentAccountsBalanceClosed,FreeTrial,MonthlyPayments,AuthenticateAgentPhone,MtnPayTo,AgentRequest, AgentRequestLimit,SetUpMeeting,Complains,HoldAccounts

admin.site.register(HoldAccounts)
admin.site.register(Complains)
admin.site.register(AgentRequest)
admin.site.register(SetUpMeeting)
admin.site.register(AgentRequestLimit)
admin.site.register(MtnPayTo)
admin.site.register(FreeTrial)
admin.site.register(MonthlyPayments)
admin.site.register(AuthenticateAgentPhone)
admin.site.register(RegisteredForFloat)
admin.site.register(AgentAccountsBalanceClosed)
admin.site.register(AgentAccountsBalanceStarted)
admin.site.register(AgentPreregistration)
admin.site.register(GroupMessage)
admin.site.register(PrivateUserMessage)
admin.site.register(PrivateChatId)
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
admin.site.register(Notifications)
admin.site.register(AgentAccounts)
admin.site.register(AgentsFloat)
admin.site.register(Reports)
