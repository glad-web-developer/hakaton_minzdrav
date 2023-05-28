from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CheckUserSerializerOut

def get_user(session_key)-> User or bool:
    try:
        session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)
        return user
    except Exception:
        return False

class CheckUser(APIView):
    """
    апи проверяет авторизацию пользователя по его session_key
    """
    def get(self, request, session_key):
        try:
            user = get_user(session_key)
            if user:
                serializer_out = CheckUserSerializerOut(data={
                    'isLogin': True,
                    'isAdmin': user.is_superuser,
                    'userName': user.username
                })
                return Response(serializer_out.initial_data)
            return Response('Ошибка авторизации', status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            serializer_out = CheckUserSerializerOut(data={
                'isLogin': False,
            })
            return Response(serializer_out.initial_data, status=status.HTTP_401_UNAUTHORIZED)