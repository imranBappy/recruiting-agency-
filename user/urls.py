from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.email_login_view, name='login'),
    path('profile/', views.profile, name='profile'),


    # For password reset and email verification, Django has built-in views
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', 
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', 
         auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
