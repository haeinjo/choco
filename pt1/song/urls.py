from django.urls import path
from .views import SongOwnList, songOwnPerAlbum, SongOwnDetail, SongCoveredList, songCoveredPerAlbum, SongCoveredDetail, songOwnPerAlbum

urlpatterns = [
    path('own/', SongOwnList.as_view()),
    path('own/<int:pk>/', SongOwnDetail.as_view()),
    path('covered/', SongCoveredList.as_view()),
    path('covered/<int:pk>/', SongCoveredDetail.as_view()),
    path('own/album/<int:pk>/', songOwnPerAlbum),
    path('covered/album/<int:pk>', songCoveredPerAlbum),
]