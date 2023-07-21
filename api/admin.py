from django.contrib import admin
from .models import Customer, CustomerAccounts, BankDeposit, MobileMoneyDeposit, MobileMoneyWithdraw, BankWithdrawal, Reports, AddToBlockList, Fraud,  Notifications,  Floats,PrivateChatId,PrivateUserMessage,GroupMessage,AgentPreregistration,RegisteredForFloat, FreeTrial,MonthlyPayments,AuthenticateAgentPhone,MtnPayTo,SetUpMeeting,Complains,HoldAccounts, GroupOwnerMessage,GroupAgentsMessage,OwnerMtnPayTo, CheckAppVersion,  CheckOwnerAppVersion, AgentAndOwnerAccounts


admin.site.register(AgentAndOwnerAccounts)
admin.site.register(CheckOwnerAppVersion)
admin.site.register(CheckAppVersion)
admin.site.register(OwnerMtnPayTo)
admin.site.register(GroupAgentsMessage)
admin.site.register(GroupOwnerMessage)

admin.site.register(HoldAccounts)
admin.site.register(Complains)

admin.site.register(SetUpMeeting)

admin.site.register(MtnPayTo)
admin.site.register(FreeTrial)
admin.site.register(MonthlyPayments)
admin.site.register(AuthenticateAgentPhone)
admin.site.register(RegisteredForFloat)
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
admin.site.register(AddToBlockList)
admin.site.register(Fraud)

admin.site.register(Notifications)

admin.site.register(Floats)
admin.site.register(Reports)
