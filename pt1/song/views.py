from song.models import SongOwn, SongCovered
from song.serializers import SongOwnSerializer, SongCoveredSerializer
from album.models import AlbumOwn, AlbumCovered
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status


class SongOwnList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, POST - 자작곡 
    """
    queryset = SongOwn.objects.all()
    serializer_class = SongOwnSerializer


@api_view(['GET'])
def songOwnPerAlbum(request, pk):
    """
    date: 2020 - 01 - 15
    madeby: haein
    des: GET - 앨범에 수록된 자작곡
    """
    try:
        song_own_list = SongOwn.objects.filter(album=pk)
    except AlbumOwn.DoesNotExist:
        return httpResponse(status=404)
    
    #show songOwns of album which is pk
    if request.method == 'GET':
        serializer = SongOwnSerializer(song_own_list, many=True)
        return Response(serializer.data)


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


@api_view(['GET'])
def songCoveredPerAlbum(request, pk):
    """
    date: 2020 - 01 - 15
    madeby: haein
    des: GET - 앨범에 수록된 커버곡
    """
    try:
        song_covered_list = SongCovered.objects.filter(album=pk)
    except AlbumCovered.DoesNotExist:
        return httpResponse(status=404)
    
    #show songOwns of album which is pk
    if request.method == 'GET':
        serializer = SongCoveredSerializer(song_covered_list, many=True)
        return Response(serializer.data)


class SongCoveredDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, PUT, DELETE - 커버곡
    """
    queryset = SongCovered.objects.all()
    serializer_class = SongCoveredSerializer


# @api_view(['GET'])
# def songList(request):
#     """
#     date: 2020 - 01 - 16
#     madeby: haein
#     des: GET - 전체곡
#     """
#     if request.method == 'GET':
#         serializer = SongSerializer(many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)