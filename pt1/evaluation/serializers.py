from rest_framework import serializers
from .models import Tag, SongOwnTag, SongCoveredTag


class TagSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: 태그 serializer
    """
    class Meta:
        model = Tag
        field = '__all__'


class SongOwnTagSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: 자작곡 - 태그 serializer
    """
    class Meta:
        model = SongOwnTag
        field = '__all__'


class SongCoveredSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: 커버곡 - 태그 serializer
    """
    class Meta:
        model = SongCoveredTag
        field = '__all__'