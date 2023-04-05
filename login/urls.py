from django.contrib import admin
from django.urls import include, path

import landingPage.views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    # path('loginUser/', views.loginUser, name='loginUser'),
]
