from django.urls import path
from .views import AlbumOwnList, AlbumOwnDetail, AlbumCoveredList, AlbumCoveredDetail

urlpatterns = [
    path('own/', AlbumOwnList.as_view()),
    path('own/<int:pk>/', AlbumOwnDetail.as_view()),
    path('covered/', AlbumCoveredList.as_view()),
    path('covered/<int:pk>', AlbumCoveredDetail.as_view()),
]