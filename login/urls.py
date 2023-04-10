from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

import home.views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    # path('passwordrecovery/', views.passwordRecovery, name='passwordRecovery'),
    path('questions/', views.securityQuestions, name='securityQuestions'),
    path('passwordrecovery/', auth_views.PasswordResetView.as_view(
        template_name='passwordRecovery.html'), name='password_reset'),
    path('passwordrecoverydone/', auth_views.PasswordResetDoneView.as_view(
        template_name='passwordRecoveryDone.html'), name='password_reset_done'),
    path('changeconfirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='changePassword.html'), name='password_reset_confirm'),
    # path('/<int:pk>/update', views.ProfileUpdateView.as_view(), name='setPassword'),
    #path('newpass/', views.newPassword, name='newPassword'),
]
