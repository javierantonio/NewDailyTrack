from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

import home.views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    # path('passwordrecovery/', views.passwordRecovery, name='passwordRecovery'),
    path('questions/', views.securityQuestions, name='securityQuestions'),
    # path('changepassword/', views.changePassword, name='changePassword'),
    # path('newpass/', views.newPassword, name='newPassword'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='passwordRecovery.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
