from rest_framework import serializers
from .models import CUser


class UserSerializer(serializers.ModelSerializer):
    """
    date: 2019 - 12 - 11
    madeby: haein
    des: 사용자 serializer
    """
    class Meta:
        model = CUser
        fields = '__all__'