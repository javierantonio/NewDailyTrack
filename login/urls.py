from django.contrib import admin
from django.urls import include, path

import home.views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('passwordrecovery/', views.passwordRecovery, name='passwordRecovery'),
    path('questions/', views.securityQuestions, name='securityQuestions'),
    path('changepassword/', views.changePassword, name='changePassword'),
    path('newpass/', views.newPassword, name='newPassword'),
]
