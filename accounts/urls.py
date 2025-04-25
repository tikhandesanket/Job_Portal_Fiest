from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Using auth_views for logout
    path('home/', views.home_view, name='home'),
    path('redirect-dashboard/', views.redirect_dashboard, name='redirect_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # define view
]