from django.urls import path

from .views import mainsiteMapView

app_name = "mainsite"

urlpatterns = [
    path("", mainsiteMapView.as_view()),
]