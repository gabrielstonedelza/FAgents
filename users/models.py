from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.conf import settings
import random

DeUser = settings.AUTH_USER_MODEL
USER_TYPE = (
    ("Owner", "Owner"),
    ("Agent", "Agent"),
    ("Administrator", "Administrator"),
)


class User(AbstractUser):
    user_type = models.CharField(max_length=50, choices=USER_TYPE,default="Agent")
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30, unique=True)
    user_blocked = models.BooleanField(default=False)
    owner = models.CharField(max_length=100)
    agent_unique_code = models.CharField(max_length=15,unique=True)
    user_approved = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email','user_type', 'full_name', 'phone_number','owner']
    USERNAME_FIELD = 'username'

    def get_username(self):
        return self.username

    def save(self, *args, **kwargs):
        a_unique = "EA"
        a_code = a_unique + str(random.randint(0,9999)) + self.phone_number[4:6]+ self.user_type[:2]
        self.agent_unique_code = a_code
        super().save(*args, **kwargs)


class AdminProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="admin_profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")

    def get_username(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    def get_profile_pic(self):
        if self.profile_pic:
            return "https://fnetagents.xyz" + self.profile_pic.url
        return ''

    def get_email(self):
        return self.user.email

    def get_phone_number(self):
        return self.user.phone_number

    def get_full_name(self):
        return self.user.full_name


class OwnerProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="owner_profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")
    owner = models.CharField(max_length=100, default="admin", blank=True)

    def get_username(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    def get_profile_pic(self):
        if self.profile_pic:
            return "https://fnetagents.xyz" + self.profile_pic.url
        return ''

    def get_email(self):
        return self.user.email

    def get_phone_number(self):
        return self.user.phone_number

    def get_full_name(self):
        return self.user.full_name


class AgentProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="agent_profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")
    owner = models.CharField(max_length=100, default="", blank=True)

    def get_owner(self):
        return self.user.owner.username

    def get_username(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    def get_profile_pic(self):
        if self.profile_pic:
            return "https://fnetagents.xyz" + self.profile_pic.url
        return ''

    def get_email(self):
        return self.user.email

    def get_phone_number(self):
        return self.user.phone_number

    def get_full_name(self):
        return self.user.full_name

    def save(self, *args, **kwargs):
        self.owner = self.user.owner
        super().save(*args, **kwargs)
