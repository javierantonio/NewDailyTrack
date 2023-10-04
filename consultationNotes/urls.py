from django.contrib import admin
from django.http import request
from django.urls import path, include
from . import views

urlpatterns = [

    path('notes/<str:userId>/', views.notesHome, name='notes'),
    path('entries/', views.viewEntries, name='notesEntries'),
    path('entries/<str:userId>/', views.viewEntries, name='noteView'),
    path('entries/<str:userId>/<int:entryId>/', views.viewEntries, name='noteView'),
    # path('delete_JournalEntry/<int:entry_id>/', views.deleteJournalEntry, name='delete_journalEntry'),
    # path('viewJournalEntry/<int:entry_id>/', views.viewJournalEntry, name='viewJournalEntry'),
    # path('star/', views.starJournalEntry, name='starJournalEntry'),
    # path('starred/', views.starredJournalEntry, name='starredJournalEntry'),


]
