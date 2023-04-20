from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.conf import settings
import random

DeUser = settings.AUTH_USER_MODEL
USER_TYPE = (
    ("Supervisor", "Supervisor"),
    ("Agent", "Agent"),
    ("Administrator", "Administrator"),
)


class User(AbstractUser):
    user_type = models.CharField(max_length=50, choices=USER_TYPE,default="Agent")
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30, unique=True)
    user_blocked = models.BooleanField(default=False)
    supervisor = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    agent_unique_code = models.CharField(max_length=500,unique=True)

    def save(self, *args, **kwargs):
        self.agent_unique_code = self.username[:5] + str(random.randint(1, 500))
        super().save(*args, **kwargs)

    REQUIRED_FIELDS = ['email','user_type', 'username', 'full_name', 'phone_number']
    USERNAME_FIELD = 'agent_unique_code'

    def get_username(self):
        return self.username


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


class SupervisorProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="supervisor_profile")
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


class AgentProfile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="agent_profile")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")

    def get_supervisor(self):
        return self.user.supervisor.username

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
