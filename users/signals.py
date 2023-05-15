from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OwnerProfile, AgentProfile, AdminProfile

DeUser = settings.AUTH_USER_MODEL


@receiver(post_save, sender=DeUser)
def create_profile(sender, created, instance, **kwargs):
    if created and instance.user_type == "Owner":
        OwnerProfile.objects.create(user=instance)
    if created and instance.user_type == "Agent":
        AgentProfile.objects.create(user=instance)
    if created and instance.user_type == "Administrator":
        AdminProfile.objects.create(user=instance)
