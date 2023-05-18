from rest_framework import serializers


class CheckUserSerializerOut(serializers.Serializer):
    isLogin = serializers.BooleanField()
    isAdmin = serializers.BooleanField()
    userName = serializers.CharField()
