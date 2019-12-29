from django.urls import path
from .views import TagList, TagDetail, SongOwnTagList, SongOwnTagDetail, SongCoveredTagList, SongCoveredTagDetail

urlpatterns = [
    path('tag/', TagList.as_view()),
    path('tag/<int:pk>', TagDetail.as_view()),
    path('own/tag', SongOwnTagList.as_view()),
    path('own/tag/<int:pk>', SongOwnTagDetail.as_view()),
    path('covered/tag', SongCoveredTagList.as_view()),
    path('covered/tag/<int:pk>', SongCoveredTagDetail.as_view()),
]

# SongOwnTagDetail, songCoveredTagDetail have to be modified.