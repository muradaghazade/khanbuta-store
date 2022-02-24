from pickle import TRUE
from django.shortcuts import render
# from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from accounts.seralizers import UserRegisterSerializer, UserSerializer, MyTokenObtainPairSerializer, AvenueSerializer, StreetSerializer
from accounts.models import Avenue, User, Street
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from products.models import Wishlist


class RegisterUserAPI(CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer

    # def perform_create(self, serializer):
        # Wishlist.objects.create(user)
        # return super().perform_create(serializer)


class UpdateUserView(APIView):
    def patch(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        user.delete()
        return Response("User deleted", status=status.HTTP_204_NO_CONTENT)


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


class AvenueByCityAPIView(APIView):
    def get(self, request, *args, **kwargs):
        avenue = Avenue.objects.filter(city__pk=kwargs['pk'])
        serializer = AvenueSerializer(avenue, many=True)
        return Response(serializer.data)

    
class AvenueByRegionAPIView(APIView):
    def get(self, request, *args, **kwargs):
        avenue = Avenue.objects.filter(region__pk=kwargs['pk'])
        serializer = AvenueSerializer(avenue, many=True)
        return Response(serializer.data)


class StreetByAvenueAPIView(APIView):
    def get(self, request, *args, **kwargs):
        street = Street.objects.filter(avenue__pk=kwargs['pk'])
        serializer = StreetSerializer(street, many=True)
        return Response(serializer.data)