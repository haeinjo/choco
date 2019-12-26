from .models import Tag, SongOwnTag, SongCoveredTag
from .serializers import TagSerializer, SongOwnTagSerializer, SongCoveredTagSerializer
from rest_framework import generics


class TagList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: GET, POST - 태그
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: GET, PUT, DELETE - 태그
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SongOwnTagList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: GET, POST - 자작곡 - 태그
    """
    queryset = SongOwnTag.objects.all()
    serializer_class = SongOwnTagSerializer


class SongOwnTagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: GET, PUT, DELETE - 자작곡 - 태그
    """
    queryset = SongOwnTag.objects.all()
    serializer_class = SongOwnTagSerializer


class SongCoveredList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: GET, POST - 커버곡 - 태그
    """    
    queryset = SongCoveredTag
    serializer_class = SongCoveredTagSerializer


class SongCoveredDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: GET, PUT, DELETE - 자작곡 - 태그
    """
    queryset = SongCoveredTag
    serializer_class = SongCoveredTagSerializer
    