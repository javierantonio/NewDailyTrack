from django.contrib import admin
from django.urls import include, path

import home.views
from . import views
import login.views

urlpatterns = [
    path('', views.steppingStoneStart, name='steppingStones'),
    path('', views.emoticard, name='emoticard'),#for debugging purpose only
    path('emoticards/<str:userId>/', views.emoticardList, name='emoticardList'),

]
