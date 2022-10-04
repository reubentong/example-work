from django.urls import path
from .views import film


urlpatterns = [
    path('film/', film, name="films")
]
