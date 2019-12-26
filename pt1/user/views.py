from user.models import CUser
from user.serializers import UserSerializer
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, POST - 사용자
    """
    queryset = CUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: GET, PUST, DELETE - 사용자
    """
    queryset = CUser.objects.all()
    serializer_class = UserSerializer