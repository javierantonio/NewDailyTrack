from django.contrib import admin
from django.http import request
from django.urls import path, include
from . import views

urlpatterns = [

    path('notes/', views.notesHome, name='notesDev'),           # for development purposes only
    path('notes/<str:userId>/', views.notesHome, name='notes'),
    path('entries/', views.viewEntries, name='notesEntries'),
    path('entries/<str:userId>/', views.viewEntries, name='noteView'),
    path('entries/<str:userId>/<int:entryId>/', views.viewEntries, name='noteView'),
    path('delete/<int:entry_id>/', views.deleteNotes, name='delete'),
    path('view/<int:entry_id>/', views.viewNotes, name='view'),
    # path('star/', views.starJournalEntry, name='starJournalEntry'),
    # path('starred/', views.starredJournalEntry, name='starredJournalEntry'),


]
