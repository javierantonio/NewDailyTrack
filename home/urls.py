from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('logout/', views.logoutView, name='logoutView')

]
