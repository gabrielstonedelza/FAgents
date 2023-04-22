from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path("activate/<uid>/<token>/",TemplateView.as_view(template_name="users/activation.html")),
    path("reset_password/",TemplateView.as_view(template_name="users/password_reset.html")),
    # path('', TemplateView.as_view(template_name="index.html")),
    # path('activate/<uid>/<token>/', TemplateView.as_view(template_name="index.html")),
    path('password/reset/confirm/<uid>/<token>/', TemplateView.as_view(template_name="users/password_reset_confirm.html")),
    # path('email/reset/confirm/<uid>/<token>/', TemplateView.as_view(template_name="index.html")),
    path('get_user_details/', views.get_user),
    path('get_supervisors_profile/', views.get_supervisors_profile),
    path('get_all_supervisors/', views.get_all_supervisors),
    path('get_all_agents/', views.get_all_agents),
    path('get_agents_profile/', views.get_agents_profile),
    path('get_admins_profile/', views.get_admins_profile),
    path('update_supervisor_profile/', views.update_supervisor_profile),
    path('update_agents_profile/', views.update_agents_profile),
    path('update_admins_profile/', views.update_admins_profile),
    path('update_user_details/', views.update_user_details),
    path('all_agents/', views.GetAllAgents.as_view()),
]