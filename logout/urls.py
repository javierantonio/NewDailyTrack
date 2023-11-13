from django.contrib import admin
from django.urls import include, path

import home.views
from . import views
import login.views

urlpatterns = [
    path('logout/', views.logoutUser, name='logout'),
]
