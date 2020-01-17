from rest_framework import serializers
from .models import SongOwn, SongCovered, SongRecommended


class SongOwnSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: 자작곡 serializer
    """
    class Meta:
        model = SongOwn
        fields = '__all__'


class SongCoveredSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: 커버곡 serializer
    """
    class Meta:
        model = SongCovered
        fields = '__all__'


class SongRecommendedSerializer(serializers.ModelSerializer):
    """
    date: 2020 - 01 - 17
    madeby: haein
    des: 추천곡 serializer
    """
    class Meta:
        model = SongRecommended
        fields = '__all__'

        
# class SongSerializer(serializers.Serializer):
#     def __init__(self, *args, **kwargs):
#         super(SongSerializer, self).__init__(*args, **kwargs)

#     songOwn = serializers.SerializerMethodField('get_songOwn')
#     songCovered = serializers.SerializerMethodField('get_songCovered')

#     def get_songOwn(self, obj):
#         return SongOwnSerializer(SongOwn.objects.all(), many=True).data

#     def get_songCovered(self, obj):
#         return SongCoveredSerializer(SongCovered.objects.all(), many=True).data