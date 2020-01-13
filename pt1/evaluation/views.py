from .models import Tag, SongOwnTag, SongCoveredTag, ScoreOwn, ScoreCovered
from .serializers import TagSerializer, SongOwnTagSerializer, SongCoveredTagSerializer, ScoreOwnSerializer, ScoreCoveredSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
 

# have to be modified
class SongOwnTagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: GET, PUT, DELETE - 자작곡 - 태그
    """
    queryset = SongOwnTag.objects.all()
    serializer_class = SongOwnTagSerializer


class SongCoveredTagList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: GET, POST - 커버곡 - 태그
    """    
    queryset = SongCoveredTag.objects.all()
    serializer_class = SongCoveredTagSerializer


# have to be modified
class SongCoveredTagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: GET, PUT, DELETE - 자작곡 - 태그
    """
    queryset = SongCoveredTag.objects.all()
    serializer_class = SongCoveredTagSerializer
    

class ScoreOwnList(generics.ListCreateAPIView):
    """
    date: 2020 - 01 - 13
    madeby: haein
    des: GET, POST - 자작곡 - 점수
    """
    queryset = ScoreOwn.objects.all()
    serializer_class = ScoreOwnSerializer


class ScoreOwnDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2020 - 01 - 13
    madeby: haein
    des: GET, PUT, DELETE - 자작곡 - 점수
    """
    queryset = ScoreOwn.objects.all()
    serializer_class = ScoreOwnSerializer


class ScoreCoveredList(generics.ListCreateAPIView):
    """
    date: 2020 - 01 - 13
    madeby: haein
    des: GET, POST - 커버곡 - 점수
    """
    queryset = ScoreCovered.objects.all()
    serializer_class = ScoreCoveredSerializer


class ScoreCoveredDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2020 - 01 - 13
    madeby: haein
    des: GET, PUT, DELETE - 커버곡 - 점수
    """
    queryset = ScoreCovered.objects.all()
    serializer_class = ScoreCoveredSerializer