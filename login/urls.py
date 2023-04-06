from django.contrib import admin
from django.urls import include, path

import home.views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
]
