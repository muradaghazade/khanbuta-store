from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from accounts.seralizers import UserRegisterSerializer, MyTokenObtainPairSerializer
from accounts.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

class RegisterUserAPI(CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer