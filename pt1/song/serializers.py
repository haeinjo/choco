from rest_framework import serializers
from .models import SongOwn, SongCovered


class SongOwnSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: 자작곡 serializer
    """
    class Meta:
        model = SongOwn
        field = '__all__'


class SongCoveredSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: 커버곡 serializer
    """
    class Meta:
        model = SongCovered
        field = '__all__'