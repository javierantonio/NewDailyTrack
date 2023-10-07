from django.contrib import admin
from django.http import request
from django.urls import path, include
from . import views

urlpatterns = [
    # path('notes/', views.notesHome, name='notesDev'), # for development purposes only
    path('create/<str:userId>/', views.notesHome, name='notesCreate'),
    # path('entries/', views.viewEntries, name='notesEntries'),
    path('entries/<str:userId>/', views.viewEntries, name='noteView'),
    path('entries/<str:userId>/o/<str:entryId>/', views.openEntry, name='noteOpen'),
    path('delete/<str:entryId>/', views.deleteNotes, name='delete'),
]
