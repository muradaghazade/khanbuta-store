from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Category, SubCategory, SubSubCategory, Logo, HeaderText, Filter
from .serializers import FilterSerializer, SubCategorySerializer, SubSubCategorySerializer, LogoSerializer, HeaderTextSerializer, FilterSerializer


class CategoryBySubAPIView(APIView):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(SubCategory, category__slug=kwargs['slug'], slug=kwargs['slug2'])
        serializer = SubCategorySerializer(category)
        return Response(serializer.data)
       


class CategoryBySubSubAPIView(APIView):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(SubSubCategory, category__category__slug=kwargs['slug'], category__slug=kwargs['slug2'], slug=kwargs['slug3'])
        serializer = SubSubCategorySerializer(category)
        return Response(serializer.data)


class LastLogoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        logo = Logo.objects.order_by("-id").first()
        serializer = LogoSerializer(logo)
        return Response(serializer.data)


class LastHeaderTextAPIView(APIView):
    def get(self, request, *args, **kwargs):
        text = HeaderText.objects.order_by("-id").first()
        serializer = HeaderTextSerializer(text)
        return Response(serializer.data)


class FiltersBySubSubAPIView(APIView):
    def get(self, request, *args, **kwargs):
        f = Filter.objects.filter(sub_sub_category__pk=kwargs['id'])
        serializer = FilterSerializer(f, many=True)
        return Response(serializer.data)
