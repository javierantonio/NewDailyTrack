from django.contrib import admin
from django.http import request
from django.urls import path, include
from . import views

urlpatterns = [

    path('unconfirmed/', views.unconfirmedList, name='unconfirmed-list'),
    path('confirmed/', views.confirmedList, name='confirmed-list'),

]
