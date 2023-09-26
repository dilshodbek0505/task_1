from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import (
    UserSerializer,
    UserUpdateSeriaizer
)
from .models import User


class UserApi(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserEditApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserUpdateSeriaizer
    queryset = User.objects.all()


class LogoutApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(token = refresh_token)
            token.blacklist()
            logout(request)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)