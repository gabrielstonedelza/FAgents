from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Customer, CustomerAccounts, BankDeposit, MobileMoneyDeposit, MobileMoneyWithdraw, BankWithdrawal, PaymentForReBalancing, Reports, AddToBlockList, Fraud, AgentReBalancing, Notifications,PrivateUserMessage,GroupMessage,AgentPreregistration
from users.models import User

DeUser = settings.AUTH_USER_MODEL

@receiver(post_save,sender=AgentReBalancing)
def alert_agent_reBalance(sender,created,instance,**kwargs):
    title = "New Agent ReBalancing"
    message = f"{instance.agent.username} wants rebalancing"
    tag = "Agent ReBalancing"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent,
                                     notification_to=admin_user,
                                     notification_tag=tag)


@receiver(post_save,sender=PaymentForReBalancing)
def alert_payment_for_reBalancing(sender,created,instance,**kwargs):
    title = "New Payment For ReBalancing"
    message = f"{instance.agent.username} just made a payment for balancing"
    tag = "Payment For ReBalancing"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent, notification_to=admin_user,
                                     notification_tag=tag)


@receiver(post_save,sender=AgentPreregistration)
def alert_agent_preregistration(sender,created,instance,**kwargs):
    title = "New Agent Preregistration"
    message = f"{instance.name} just wants a setup"
    tag = "PreRegistration"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=admin_user, notification_to=admin_user,
                                     notification_tag=tag)


@receiver(post_save,sender=BankDeposit)
def alert_bank_deposit(sender,created,instance,**kwargs):
    title = "New bank deposit"
    message = f"{instance.agent.username} just made a bank deposit of {instance.amount}"
    tag = "Bank Deposit"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.user, notification_to=admin_user,
                                     notification_tag=tag)

@receiver(post_save,sender=MobileMoneyDeposit)
def alert_momo_deposit(sender,created,instance,**kwargs):
    title = "New momo deposit"
    message = f"{instance.agent.username} just made a momo deposit of {instance.amount}"
    tag = "Momo Deposit"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent, notification_to=admin_user,
                                     notification_tag=tag)


@receiver(post_save,sender=MobileMoneyWithdraw)
def alert_momo_withdrawal(sender,created,instance,**kwargs):
    title = "New momo withdrawal"
    message = f"{instance.agent.username} just made a momo withdrawal of {instance.amount}"
    tag = "Momo Withdrawal"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.user, notification_to=admin_user,
                                     notification_tag=tag)

@receiver(post_save,sender=BankWithdrawal)
def alert_bank_withdrawal(sender,created,instance,**kwargs):
    title = "New bank withdrawal"
    message = f"{instance.agent.username} just made a bank withdrawal of {instance.amount}"
    tag = "Bank Withdrawal"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.user, notification_to=admin_user,
                                     notification_tag=tag)

@receiver(post_save,sender=Reports)
def alert_report(sender,created,instance,**kwargs):
    title = "New report"
    message = f"{instance.agent.username} just added new report"
    tag = "Report"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.user, notification_to=admin_user,
                                     notification_tag=tag)

@receiver(post_save,sender=Fraud)
def alert_fraud(sender,created,instance,**kwargs):
    title = "New fraud alert"
    message = f"{instance.agent.username} just added a fraud alert"
    tag = "Fraud"
    users = User.objects.exclude(id=instance.agent.id)

    if created:
        for i in users:

            Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                         notification_message=message, notification_from=instance.user, notification_to=i,
                                         notification_tag=tag)


@receiver(post_save, sender=GroupMessage)
def alert_pub_message(sender, created, instance, **kwargs):
    title = f"New group message"
    message = f"{instance.user.username} sent a message to the group"
    transaction_type = "New group message"

    users = User.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(item_id=instance.id, transaction_type=transaction_type,
                                         notification_title=title, notification_message=message,
                                         notification_from=instance.user, user2=i,
                                         )


@receiver(post_save, sender=PrivateUserMessage)
def alert_private_message(sender, created, instance, **kwargs):
    title = f"New private message"
    transaction_type = "New private message"

    if created:
        if instance.sender:
            message = f"{instance.sender.username} sent you a message"
            Notifications.objects.create(item_id=instance.id, notification_title=title,
                                         notification_message=message, transaction_type=transaction_type,
                                         user2=instance.receiver)
        if instance.receiver:
            message = f"{instance.receiver.username} sent you a message"
            Notifications.objects.create(item_id=instance.id, notification_title=title,
                                         notification_message=message, transaction_type=transaction_type,
                                         user2=instance.sender)