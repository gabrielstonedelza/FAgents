from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import User, SupervisorProfile, AdminProfile, AgentProfile


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'password', 'phone_number', 'full_name', 'user_type','supervisor','agent_unique_code']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone_number', 'full_name']


class SupervisorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorProfile
        fields = ['id', 'user', 'profile_pic', 'get_username', 'get_profile_pic', 'get_email', 'get_phone_number',
                  'get_full_name']
        read_only_fields = ['user']


class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = ['id', 'user', 'profile_pic', 'get_username', 'get_profile_pic', 'get_email', 'get_phone_number',
                  'get_full_name']
        read_only_fields = ['user']


class AgentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ['id', 'user', 'profile_pic', 'get_username', 'get_profile_pic', 'get_email', 'get_phone_number',
                  'get_full_name','supervisor',]
        read_only_fields = ['user']
