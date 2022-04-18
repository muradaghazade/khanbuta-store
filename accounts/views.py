from accounts.utils import send_sms
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from accounts.seralizers import UserRegisterSerializer, UserSerializer, MyTokenObtainPairSerializer, AvenueSerializer, StreetSerializer, BuyerSerializer, UserSubSubCategorySerializer, UserCategorySerializer, UserSubCategorySerializer, UserShowSerializer, ResetPasswordSerializer, ForgetPasswordSerializer, ResetPasswordTwoSerializer, RegionSerializer
from accounts.models import Avenue, User, Street, UserSubSubCategory, UserCategory, UserSubCategory, OTPCode, Region
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from products.models import Cart, Product, Wishlist
from products.paginations import CustomPagination
from django.db.models import Q
from products.serializers import VendorSerializer


class UserCategoryAPIView(ListAPIView):
    model = UserCategory
    serializer_class = UserCategorySerializer
    queryset = UserCategory.objects.order_by("-id")


class CategoryBySubAPIView(APIView):
    def get(self, request, *args, **kwargs):
        category = UserSubCategory.objects.filter(category__id=kwargs['id'])
        serializer = UserSubCategorySerializer(category, many=True)
        return Response(serializer.data)
       

class CategoryBySubSubAPIView(APIView):
    def get(self, request, *args, **kwargs):
        category = UserSubSubCategory.objects.filter(category__id=kwargs['id'])
        serializer = UserSubSubCategorySerializer(category, many=True)
        return Response(serializer.data)


class RegisterUserAPI(CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Wishlist.objects.create(user=user)
        Cart.objects.create(user=user)


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
        serializer = VendorSerializer(user)
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


class RegionByCityAPIView(APIView):
    def get(self, request, *args, **kwargs):
        street = Region.objects.filter(city__pk=kwargs['pk'])
        serializer = RegionSerializer(street, many=True)
        return Response(serializer.data)


class GetAllStores(ListAPIView):
    model = User
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    queryset = User.objects.filter(is_store=True, is_vendor=False)

    def get_queryset(self):
        az = self.request.data.get('az')
        za = self.request.data.get('za')
        min_rating = self.request.data.get('min_rating')
        max_rating = self.request.data.get('max_rating')
        category = self.request.data.get('category')
        city = self.request.data.get('city')
        region = self.request.data.get('region')
        title = self.request.data.get('title')
        sub_category = self.request.data.get('sub_category')
        sub_sub_category = self.request.data.get('sub_sub_category')
        queryset = User.objects.filter(is_store=True, is_vendor=False)

        if title:
            queryset = queryset.filter(title__icontains=title)

        if category:
            queryset = queryset.filter(category__title__icontains=category)

        if city:
            queryset = queryset.filter(city__title__icontains=city)

        if region:
            queryset = queryset.filter(region__title__icontains=region)

        if sub_category:
            queryset = queryset.filter(sub_category__title__icontains=sub_category)

        if sub_sub_category:
            queryset = queryset.filter(sub_sub_category__title__icontains=sub_sub_category)

        if az:
            queryset = queryset.order_by('title')

        if za:
            queryset = queryset.order_by('-title')

        if min_rating:
            queryset = queryset.order_by('rating')

        if max_rating:
            queryset = queryset.order_by('-rating')
        
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetAllVendors(ListAPIView):
    model = User
    serializer_class = VendorSerializer
    pagination_class = CustomPagination
    queryset = User.objects.filter(is_store=False, is_vendor=True).order_by("-id")

    def get_queryset(self):
        # az = self.request.data.get('az')
        # za = self.request.data.get('za')
        # min_rating = self.request.data.get('min_rating')
        # max_rating = self.request.data.get('max_rating')
        # category = self.request.data.get('category')
        title = self.request.data.get('title')
        # sub_category = self.request.data.get('sub_category')
        # sub_sub_category = self.request.data.get('sub_sub_category')
        queryset = User.objects.filter(is_store=False, is_vendor=True).order_by("-id")

        if title:
            queryset = queryset.filter(title__icontains=title)

        # if category:
        #     queryset = queryset.filter(category__title__icontains=category)

        # if sub_category:
        #     queryset = queryset.filter(sub_category__title__icontains=category)

        # if sub_sub_category:
        #     queryset = queryset.filter(sub_sub_category__title__icontains=category)

        # if az:
        #     queryset = queryset.order_by('title')

        # if za:
        #     queryset = queryset.order_by('-title')

        # if min_rating:
        #     queryset = queryset.order_by('rating')

        # if max_rating:
        #     queryset = queryset.order_by('-rating')
        
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetMixedStoresVendors(ListAPIView):
    model = User
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    queryset = User.objects.filter(Q(is_vendor=True) | 
                               Q(is_store=True))

    def get_queryset(self):
        category = self.request.data.get('category')
        title = self.request.data.get('title')
        sub_category = self.request.data.get('sub_category')
        sub_sub_category = self.request.data.get('sub_sub_category')
        queryset = User.objects.filter(Q(is_vendor=True) | 
                               Q(is_store=True))
                               
        if title:
            queryset = queryset.filter(title__icontains=title)

        if category:
            queryset = queryset.filter(category__title__icontains=category)

        if sub_category:
            queryset = queryset.filter(sub_category__title__icontains=category)

        if sub_sub_category:
            queryset = queryset.filter(sub_sub_category__title__icontains=category)
        
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ForgetPasswordAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ForgetPasswordSerializer

    def post(self, request):
        user = User.objects.filter(number=request.data.get('number')).first()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = OTPCode.objects.filter(user=user).first()
        send_sms(otp.code, user.number)
        return Response({
            'status': 'success',
            'message': 'OTP sent successfully'
        }, status=status.HTTP_200_OK)


class ResetPasswordTwoAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ResetPasswordTwoSerializer

    def post(self, request):
        user = User.objects.filter(number=request.data.get('number')).first()
        otp_code = OTPCode.objects.filter(user=user).first()
        if otp_code.code != request.data.get('code'):
            return Response({
                'status': 'error',
                'message': 'Invalid OTP'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(request.data.get('password'))
        user.save()
        return Response({
            'status': 'success',
            'message': 'Password reset successfully'
        }, status=status.HTTP_200_OK) 


class ResetPasswordAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        user = User.objects.filter(number=request.data.get('number')).first()
        # otp_code = OTPCode.objects.filter(user=user).first()
        # if otp_code.code != request.data.get('code'):
        #     return Response({
        #         'status': 'error',
        #         'message': 'Invalid OTP'
        #     }, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(request.data.get('password'))
        user.save()
        return Response({
            'status': 'success',
            'message': 'Password reset successfully'
        }, status=status.HTTP_200_OK) 