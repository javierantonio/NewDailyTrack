from django.urls import include, path

urlpatterns = [
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]