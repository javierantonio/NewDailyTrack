from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='registrationhomepage'),
    path('viewuserstable/', views.viewusers, name='viewuserstable'),
    path('viewpatientstable/', views.viewpatients, name='viewpatientstable'),
    path('viewspecialiststable/',
         views.viewspecialists,
         name='viewspecialiststable'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('userregistration', views.userRegistration, name='userregistration'),
]
