from .models import Tag, SongOwnTag, SongCoveredTag, ScoreOwn, ScoreCovered
from .serializers import TagSerializer, SongOwnTagSerializer, SongCoveredTagSerializer, ScoreOwnSerializer, ScoreCoveredSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

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
 

@api_view(['GET', 'DELETE'])
def songOwnTagDetail(request, pk):
    try:
        song_own_tag_list = SongOwnTag.objects.filter(song=pk)
    except SongOwnTag.DoesNotExist:
        return httpResponse(status=404)
    
    #show SongOwnTags including SongOwns by pk
    if request.method == 'GET':
        serializer = SongOwnTagSerializer(song_own_tag_list, many=True)
        return Response(serializer.data)
    
    #delete SongOwnTags
    if request.method == 'DELETE':
        try:
            song_own_tag = SongOwnTag.objects.get(id=pk)
        except SongOwnTag.DoewNotExist:
            return httpResponse(status=404)
        song_own_tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# # have to be modified
# class SongOwnTagDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     date: 2019 - 12 - 13
#     madeby: haein
#     des: GET, PUT, DELETE - 자작곡 - 태그
#     """
#     queryset = SongOwnTag.objects.all()
#     serializer_class = SongOwnTagSerializer


class SongCoveredTagList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: GET, POST - 커버곡 - 태그
    """    
    queryset = SongCoveredTag.objects.all()
    serializer_class = SongCoveredTagSerializer


@api_view(['GET', 'DELETE'])
def songCoveredTagDetail(request, pk):
    try:
        song_covered_tag_list = SongCoveredTag.objects.filter(song=pk)
    except SongCoveredTag.DoesNotExist:
        return httpResponse(status=404)
    
    #show SongOwnTags including SongOwns by pk
    if request.method == 'GET':
        serializer = SongCoveredTagSerializer(song_covered_tag_list, many=True)
        return Response(serializer.data)
    
    #delete SongOwnTags
    if request.method == 'DELETE':
        try:
            song_covered_tag = SongCoveredTag.objects.get(id=pk)
        except SongCoveredTag.DoewNotExist:
            return httpResponse(status=404)
        song_covered_tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# have to be modified
# class SongCoveredTagDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     date: 2019 - 12 - 13
#     madeby: haein
#     des: GET, PUT, DELETE - 자작곡 - 태그
#     """
#     queryset = SongCoveredTag.objects.all()
#     serializer_class = SongCoveredTagSerializer
    

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