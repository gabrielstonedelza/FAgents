from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    # path('email/reset/confirm/<uid>/<token>/', TemplateView.as_view(template_name="index.html")),
    path('get_user_details/', views.get_user),
    path('get_supervisors_profile/', views.get_owners_profile),
    path('get_all_supervisors/', views.get_all_supervisors),
    path('get_de_admin/', views.get_de_admin),
    path('get_all_agents/', views.get_all_agents),
    path('get_all_user/', views.get_all_user),
    path('get_agents_profile/', views.get_agents_profile),
    path('get_supervisor_with_code/<str:unique_code>/', views.get_supervisor_with_code),
    path('get_supervisor_agents/<str:supervisors_code>/', views.get_owner_agents),
    path('get_admins_profile/', views.get_admins_profile),
    path('update_supervisor_profile/', views.update_owner_profile),
    path('update_agents_profile/', views.update_agents_profile),
    path('update_admins_profile/', views.update_admins_profile),
    path('update_user_details/', views.update_user_details),
    path('all_agents/', views.GetAllAgents.as_view()),
    path('update_blocked/<int:id>/', views.update_blocked),
    path('approve_user/<int:id>/', views.approve_user),
    path('get_all_blocked_users/', views.get_all_blocked_users),
]