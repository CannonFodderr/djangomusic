from django.urls import path
from . import views

app_name="music"

urlpatterns = [
    path('', views.indexView.as_view(), name="index"),
    path('<pk>/', views.detailsView.as_view(), name="details"),
    path('album/add/', views.AlbumCreate.as_view(), name="album-add"),
    path('album/<pk>/', views.AlbumUpdate.as_view(), name="album-update"),
    path('album/<pk>/delete/', views.AlbumDelete.as_view(), name="album-delete")
]