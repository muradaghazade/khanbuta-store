from rest_framework import viewsets
from accounts.models import *
from accounts.seralizers import UserSerializer, CitySerializer, SocialMediaSerializer, SocialIconSerializer, SocialIconCreateSerializer, RegionSerializer, AvenueSerializer, StreetSerializer, BuyerSerializer, UserCategorySerializer, UserSubCategorySerializer, UserSubSubCategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UserCategoryViewSet(viewsets.ViewSet):
    queryset = UserCategory.objects.all()
    serializer_class = UserCategorySerializer

    def list(self, request):
        self.queryset = UserCategory.objects.all()
        serializers_class = UserCategorySerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(self.queryset, slug=pk)
        serializers_class = UserCategorySerializer(category)
        return Response(serializers_class.data)


class UserSubCategoryViewSet(viewsets.ViewSet):
    queryset = UserSubCategory.objects.all()
    serializer_class = UserSubCategorySerializer

    def list(self, request):
        self.queryset = UserSubCategory.objects.all()
        serializers_class = UserSubCategorySerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(self.queryset, slug=pk)
        serializers_class = UserSubCategorySerializer(category)
        return Response(serializers_class.data)


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.filter(is_store=False, is_vendor=False)
    serializer_class = BuyerSerializer

    def list(self, request):
        self.queryset = User.objects.filter(is_store=False, is_vendor=False)
        serializers_class = BuyerSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializers_class = BuyerSerializer(user)
        return Response(serializers_class.data)


class CityViewSet(viewsets.ViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request):
        self.queryset = City.objects.all()
        serializers_class = CitySerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        city = get_object_or_404(self.queryset, pk=pk)
        serializers_class = CitySerializer(city)
        return Response(serializers_class.data)


class RegionViewSet(viewsets.ViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def list(self, request):
        self.queryset = Region.objects.all()
        serializers_class = RegionSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        region = get_object_or_404(self.queryset, pk=pk)
        serializers_class = RegionSerializer(region)
        return Response(serializers_class.data)


class AvenueViewSet(viewsets.ViewSet):
    queryset = Avenue.objects.all()
    serializer_class = AvenueSerializer

    def list(self, request):
        self.queryset = Avenue.objects.all()
        serializers_class = AvenueSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        avenue = get_object_or_404(self.queryset, pk=pk)
        serializers_class = AvenueSerializer(avenue)
        return Response(serializers_class.data)


class StreetViewSet(viewsets.ViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    def list(self, request):
        self.queryset = Street.objects.all()
        serializers_class = StreetSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        street = get_object_or_404(self.queryset, pk=pk)
        serializers_class = StreetSerializer(street)
        return Response(serializers_class.data)


class SocialMediaViewSet(viewsets.ViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

    def list(self, request):
        self.queryset = SocialMedia.objects.all()
        serializers_class = SocialMediaSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        social_media = get_object_or_404(self.queryset, pk=pk)
        serializers_class = SocialMediaSerializer(social_media)
        return Response(serializers_class.data)


class SocialMediaViewSet(viewsets.ViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

    def list(self, request):
        self.queryset = SocialMedia.objects.all()
        serializers_class = SocialMediaSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        social_media = get_object_or_404(self.queryset, pk=pk)
        serializers_class = SocialMediaSerializer(social_media)
        return Response(serializers_class.data)


class SocialIconViewSet(viewsets.ModelViewSet):
    serializer_class = SocialIconCreateSerializer
    queryset = SocialIcon.objects.all()

    def list(self, request):
        self.queryset = SocialIcon.objects.all()
        serializers_class = SocialIconSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        social_icon = get_object_or_404(self.queryset, pk=pk)
        serializers_class = SocialIconSerializer(social_icon)
        return Response(serializers_class.data)


class StoreViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_store=True, is_vendor=False)

    # def list(self, request):
    #     self.queryset = User.objects.filter(is_store=True, is_vendor=False)
    #     serializers_class = UserSerializer(self.queryset, many=True)
    #     return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        social_icon = get_object_or_404(self.queryset, pk=pk)
        serializers_class = UserSerializer(social_icon)
        return Response(serializers_class.data)


class VendorViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_store=False, is_vendor=True)

    # def list(self, request):
    #     self.queryset = User.objects.filter(is_store=False, is_vendor=True)
    #     serializers_class = UserSerializer(self.queryset, many=True)
    #     return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        social_icon = get_object_or_404(self.queryset, pk=pk)
        serializers_class = UserSerializer(social_icon)
        return Response(serializers_class.data)