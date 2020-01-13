from song.models import SongOwn, SongCovered
from song.serializers import SongOwnSerializer, SongCoveredSerializer
from rest_framework import generics


class SongList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, POST - 자작곡 
    """
    queryset = SongOwn.objects.all()
    serializer_class = SongOwnSerializer


class SongOwnList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, POST - 자작곡 
    """
    queryset = SongOwn.objects.all()
    serializer_class = SongOwnSerializer


class SongOwnDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, PUT, DELETE - 자작곡
    """
    queryset = SongOwn.objects.all()
    serializer_class = SongOwnSerializer


class SongCoveredList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, POST - 커버곡 
    """
    queryset = SongCovered.objects.all()
    serializer_class = SongCoveredSerializer


class SongCoveredDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, PUT, DELETE - 커버곡
    """
    queryset = SongCovered.objects.all()
    serializer_class = SongCoveredSerializer