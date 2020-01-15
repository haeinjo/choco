from django.urls import path
from .views import (TagList, TagDetail, SongOwnTagList, SongCoveredTagList, ScoreOwnList, 
    ScoreOwnDetail, ScoreCoveredList, ScoreCoveredDetail, songOwnTagDetail, songCoveredTagDetail)

urlpatterns = [
    path('tag/', TagList.as_view()),
    path('tag/<int:pk>', TagDetail.as_view()),
    path('own/tag', SongOwnTagList.as_view()),
    path('own/tag/<int:pk>', songOwnTagDetail),
    # path('own/tag/<int:pk>', SongOwnTagDetail.as_view()),
    path('covered/tag', SongCoveredTagList.as_view()),
    path('covered/tag/<int:pk>', songCoveredTagDetail),
    path('score/own', ScoreOwnList.as_view()),
    path('score/own/<int:pk>', ScoreOwnDetail.as_view()),
    path('score/covered', ScoreCoveredList.as_view()),
    path('score/covered/<int:pk>', ScoreCoveredDetail.as_view()),
]

# SongOwnTagDetail, songCoveredTagDetail have to be modified.