from django.urls import path
from summaryReports.dashapp import app

urlpatterns = [
    path('dash-app/', app.server),
]