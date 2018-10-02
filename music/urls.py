from django.urls import path
from . import views

app_name="music"

urlpatterns = [
    path('', views.index, name="index"),
    path('<album_id>/', views.details, name="details"),
    path('<album_id>/favorite/', views.favorite, name="favorite")
]