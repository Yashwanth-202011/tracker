from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard_redirect, name='dashboard_redirect'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('log-period/', views.log_period, name='log_period'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
