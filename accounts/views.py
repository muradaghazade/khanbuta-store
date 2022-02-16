from django.shortcuts import render
# from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from accounts.seralizers import UserRegisterSerializer, UserSerializer, MyTokenObtainPairSerializer
from accounts.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse

class RegisterUserAPI(CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class GetUserDataByTokenView(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)


class VerifyNumberView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data['id']
        user_code = request.data['code']
        db_user_code = User.objects.get(pk=user_id).code.code
        user_p = User.objects.get(pk=user_id)
        refresh = RefreshToken.for_user(user_p)
        print(refresh)
        if user_code == db_user_code:
            user = User.objects.get(pk=user_id)
            user.is_verified = True
            user.save()
        else:
            return JsonResponse({"Detail":"OTP code is wrong"})
        print(db_user_code)
        # serializer = UserSerializer(user)
        return JsonResponse({"Success":"Number is verified!", "refresh":str(refresh), "access":str(refresh.access_token)})

    