from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Category, SubCategory, SubSubCategory
from .serializers import SubCategorySerializer, SubSubCategorySerializer


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
