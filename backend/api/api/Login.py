
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import LoginSerializer


class Login(APIView):
    def post(self, request, format=None):

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = authenticate(request, username=serializer.data["login"],
                                    password=serializer.data["pas"])
            except Exception:
                return Response('Ошибка авторизации. Неверный логин/пароль', status=status.HTTP_400_BAD_REQUEST)

            if user is not None:
                login(request, user)
                return Response({'sessionid':request.session.session_key}, status=status.HTTP_200_OK)

            return Response('Ошибка авторизации. Неверный логин/пароль', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)