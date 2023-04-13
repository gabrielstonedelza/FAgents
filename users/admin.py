from django.contrib import admin

from .models import User, SupervisorProfile, AdminProfile, AgentProfile

admin.site.register(User)
admin.site.register(SupervisorProfile)
admin.site.register(AdminProfile)
admin.site.register(AgentProfile)