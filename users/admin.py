from django.contrib import admin

from .models import User, OwnerProfile, AdminProfile, AgentProfile

class AdminUserProfile(admin.ModelAdmin):
    list_display = ['id','user_type','email','full_name','phone_number','username','owner','agent_unique_code']
    search_fields = ['id','user_type','email','full_name','phone_number','username','owner','agent_unique_code']

    class Meta:
        model = User

admin.site.register(User,AdminUserProfile)
admin.site.register(OwnerProfile)
admin.site.register(AdminProfile)
admin.site.register(AgentProfile)