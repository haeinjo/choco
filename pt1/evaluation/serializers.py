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