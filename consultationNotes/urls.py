from django.contrib import admin
from django.http import request
from django.urls import path, include
from . import views

urlpatterns = [

    path('notes/', views.notesHome, name='notes'),
    path('notes/entries/', views.viewEntries, name='notesEntries'),
    # path('delete_JournalEntry/<int:entry_id>/', views.deleteJournalEntry, name='delete_journalEntry'),
    # path('viewJournalEntry/<int:entry_id>/', views.viewJournalEntry, name='viewJournalEntry'),
    # path('star/', views.starJournalEntry, name='starJournalEntry'),
    # path('starred/', views.starredJournalEntry, name='starredJournalEntry'),


]
