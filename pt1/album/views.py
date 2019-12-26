from album.models import AlbumOwn, AlbumCovered
from album.serializers import AlbumOwnSerializer, AlbumCoveredSerializer
from rest_framework import generics


class AlbumOwnList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, POST - 앨범 - 자작곡
    """
    queryset = AlbumOwn.objects.all()
    serializer_class = AlbumOwnSerializer


class AlbumOwnDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, PUT, DELETE - 앨범 - 자작곡
    """
    queryset = AlbumOwn.objects.all()
    serializer_class = AlbumOwnSerializer



class AlbumCoveredList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, POST - 앨범 - 커버곡
    """
    queryset = AlbumCovered.objects.all()
    serializer_class = AlbumCoveredSerializer


class AlbumCoveredDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, PUT, DELETE - 앨범 - 커버곡
    """
    queryset = AlbumCovered.objects.all()
    serializer_class = AlbumCoveredSerializer