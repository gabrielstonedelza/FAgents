from django.contrib import admin

from .models import User, OwnerProfile, AdminProfile, AgentProfile

admin.site.register(User)
admin.site.register(OwnerProfile)
admin.site.register(AdminProfile)
admin.site.register(AgentProfile)