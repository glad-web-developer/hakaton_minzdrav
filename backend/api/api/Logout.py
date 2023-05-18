from django.contrib.auth import logout
from rest_framework.request import Request
from rest_framework.views import APIView


class Logout(APIView):
    def get(self, request):
        logout(request)
        return Request('Ок')