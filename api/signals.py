from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User
from .models import (BankDeposit, MobileMoneyDeposit, MobileMoneyWithdraw, BankWithdrawal, PaymentForReBalancing, \
    Reports, Fraud, AgentReBalancing, Notifications, PrivateUserMessage, GroupMessage, AgentPreregistration, \
    RegisteredForFloat,AgentRequest,SetUpMeeting)

DeUser = settings.AUTH_USER_MODEL

@receiver(post_save,sender=SetUpMeeting)
def alert_meeting(sender,created,instance,**kwargs):
    title = "Scheduled Online Meeting"
    message = f"{instance.administrator.username} has scheduled online meeting for {instance.date_of_meeting} {instance.time_of_meeting}"
    tag = "Owners Meeting"
    admin_user = User.objects.get(id=1)
    admin_owners = User.objects.filter(supervisor=admin_user.agent_unique_code)

    if created:
        for i in admin_owners:
            Notifications.objects.create(item_id=instance.id, notification_title=title,
                                         notification_message=message, notification_from=instance.administrator,
                                         notification_to=i,
                                         transaction_tag=tag)


@receiver(post_save,sender=AgentRequest)
def alert_agent_request(sender,created,instance,**kwargs):
    title = "New Request"
    message = f"New request from {instance.agent.username}"
    tag = "Agent Request"

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent,
                                     notification_to=instance.owner,
                                     transaction_tag=tag)
@receiver(post_save,sender=RegisteredForFloat)
def alert_request_to_join_float(sender,created,instance,**kwargs):
    title = "New Float Request"
    message = f"{instance.agent.username} wants to join float"
    tag = "Request to join float"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent,
                                     notification_to=admin_user,
                                     transaction_tag=tag)

@receiver(post_save,sender=AgentReBalancing)
def alert_agent_reBalance(sender,created,instance,**kwargs):
    title = "New Agent ReBalancing"
    message = f"{instance.agent.username} wants rebalancing"
    tag = "Agent ReBalancing"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent,
                                     notification_to=admin_user,
                                     transaction_tag=tag)


@receiver(post_save,sender=PaymentForReBalancing)
def alert_payment_for_reBalancing(sender,created,instance,**kwargs):
    title = "New Payment For ReBalancing"
    message = f"{instance.agent.username} just made a payment for balancing"
    tag = "Payment For ReBalancing"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent, notification_to=admin_user,
                                     transaction_tag=tag)


@receiver(post_save,sender=AgentPreregistration)
def alert_agent_preregistration(sender,created,instance,**kwargs):
    title = "New Agent Preregistration"
    message = f"{instance.name} just wants a setup"
    tag = "PreRegistration"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=admin_user, notification_to=admin_user,
                                     transaction_tag=tag)


@receiver(post_save,sender=BankDeposit)
def alert_bank_deposit(sender,created,instance,**kwargs):
    title = "New bank deposit"
    message = f"{instance.agent.username} just made a bank deposit of {instance.amount}"
    tag = "Bank Deposit"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent, notification_to=admin_user,
                                     transaction_tag=tag)

@receiver(post_save,sender=MobileMoneyDeposit)
def alert_momo_deposit(sender,created,instance,**kwargs):
    title = "New momo deposit"
    message = f"{instance.agent.username} just made a momo deposit of {instance.amount}"
    tag = "Momo Deposit"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent, notification_to=admin_user,
                                     transaction_tag=tag)


@receiver(post_save,sender=MobileMoneyWithdraw)
def alert_momo_withdrawal(sender,created,instance,**kwargs):
    title = "New momo withdrawal"
    message = f"{instance.agent.username} just made a momo withdrawal of {instance.amount}"
    tag = "Momo Withdrawal"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent, notification_to=admin_user,
                                     transaction_tag=tag)

@receiver(post_save,sender=BankWithdrawal)
def alert_bank_withdrawal(sender,created,instance,**kwargs):
    title = "New bank withdrawal"
    message = f"{instance.agent.username} just made a bank withdrawal of {instance.amount}"
    tag = "Bank Withdrawal"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.agent, notification_to=admin_user,
                                     transaction_tag=tag)

@receiver(post_save,sender=Reports)
def alert_report(sender,created,instance,**kwargs):
    title = "New report"
    message = f"{instance.agent.username} just added new report"
    tag = "Report"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                     notification_message=message, notification_from=instance.user, notification_to=admin_user,
                                     transaction_tag=tag)

@receiver(post_save,sender=Fraud)
def alert_fraud(sender,created,instance,**kwargs):
    title = "New fraud alert"
    message = f"{instance.agent.username} just added a fraud alert"
    tag = "Fraud"
    users = User.objects.exclude(id=instance.agent.id)

    if created:
        for i in users:
            Notifications.objects.create(item_id=instance.id, notification_title=title,
                                         notification_message=message, notification_from=instance.agent, notification_to=i,
                                         transaction_tag=tag)


@receiver(post_save, sender=GroupMessage)
def alert_pub_message(sender, created, instance, **kwargs):
    title = f"New group message"
    message = f"{instance.user.username} sent a message to the group"
    transaction_tag = "New group message"

    users = User.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(item_id=instance.id, transaction_tag=transaction_tag,
                                         notification_title=title, notification_message=message,
                                         notification_from=instance.user, notification_to=i,
                                         )


@receiver(post_save, sender=PrivateUserMessage)
def alert_private_message(sender, created, instance, **kwargs):
    title = f"New private message"
    transaction_tag = "New private message"

    if created:
        if instance.sender:
            message = f"{instance.sender.username} sent you a message"
            Notifications.objects.create(item_id=instance.id, notification_title=title,
                                         notification_message=message, transaction_tag=transaction_tag,
                                         notification_to=instance.receiver)
        if instance.receiver:
            message = f"{instance.receiver.username} sent you a message"
            Notifications.objects.create(item_id=instance.id, notification_title=title,
                                         notification_message=message, transaction_tag=transaction_tag,
                                         notification_to=instance.sender)