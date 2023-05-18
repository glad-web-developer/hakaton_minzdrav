from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    pas = serializers.CharField(required=True)
