from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='landing'),
    path('registration/', include('registration.urls'), name='registration'),
]
