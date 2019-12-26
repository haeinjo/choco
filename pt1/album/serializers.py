from rest_framework import serializers
from .models import AlbumOwn, AlbumCovered


class AlbumOwnSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: 앨범 - 자작곡 serializer
    """
    class Meta:
        model = AlbumOwn
        fields = '__all__'


class AlbumCoveredSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: 앨범 - 커버곡 serializer
    """
    class Meta:
        model = AlbumCovered
        fields = '__all__'