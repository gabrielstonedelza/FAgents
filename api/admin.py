from django.contrib import admin
from .models import Customer, CustomerAccounts, BankDeposit, MobileMoneyDeposit, MobileMoneyWithdraw, BankWithdrawal, PaymentForReBalancing, Reports, AddToBlockList, Fraud, AgentReBalancing, Notifications, AgentAccounts, Floats,PrivateChatId,PrivateUserMessage,GroupMessage,AgentPreregistration,RegisteredForFloat, AgentAccountsBalanceStarted, FreeTrial,MonthlyPayments,AuthenticateAgentPhone,MtnPayTo,AgentRequest, AgentRequestLimit,SetUpMeeting,Complains,HoldAccounts, AgentRequestPayment,AddedToApprovedRequest,AddedToApprovedPayment,AddedToApprovedReBalancing,GroupOwnerMessage,GroupAgentsMessage,OwnerMtnPayTo, CheckAppVersion, LoginTracker, CheckOwnerAppVersion

class AdminAgentAccountStartedWith(admin.ModelAdmin):
    list_display = ['id', 'agent','physical', 'mtn_e_cash', 'tigo_airtel_e_cash', 'vodafone_e_cash','e_cash_total','date_posted','time_posted']
    search_fields = ['id', 'agent','date_posted','time_posted']

    class Meta:
        model = AgentAccountsBalanceStarted

class AdminUserLoginTracker(admin.ModelAdmin):
    list_display = ['id','agent','app_version_logged_in_with','date_logged_in','time_logged_in']
    search_fields = ['id','agent','app_version_logged_in_with','date_logged_in','time_logged_in']

    class Meta:
        model = LoginTracker

admin.site.register(LoginTracker,AdminUserLoginTracker)
admin.site.register(CheckOwnerAppVersion)
admin.site.register(CheckAppVersion)
admin.site.register(OwnerMtnPayTo)
admin.site.register(GroupAgentsMessage)
admin.site.register(GroupOwnerMessage)
admin.site.register(AddedToApprovedReBalancing)
admin.site.register(AddedToApprovedRequest)
admin.site.register(AddedToApprovedPayment)
admin.site.register(AgentRequestPayment)
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
admin.site.register(AgentAccountsBalanceStarted,AdminAgentAccountStartedWith)
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
admin.site.register(Floats)
admin.site.register(Reports)
