from rest_framework import serializers
from .models import Tag, SongOwnTag, SongCoveredTag, ScoreOwn, ScoreCovered


class TagSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: 태그 serializer
    """
    class Meta:
        model = Tag
        fields = '__all__'


class SongOwnTagSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: 자작곡 - 태그 serializer
    """
    class Meta:
        model = SongOwnTag
        fields = '__all__'


class SongCoveredTagSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: 커버곡 - 태그 serializer
    """
    class Meta:
        model = SongCoveredTag
        fields = '__all__'


class ScoreOwnSerializer(serializers.ModelSerializer):
    """
    date: 2020 - 01 - 13
    madeby: haein
    des: 자작곡 - 점수 serializer
    """
    class Meta:
        model = ScoreOwn
        fields = '__all__'


class ScoreCoveredSerializer(serializers.ModelSerializer):
    """
    date: 2020 - 01 - 13
    madeby: haein
    des: 커버곡 - 점수 serializer
    """
    class Meta:
        model = ScoreCovered
        fields = '__all__'