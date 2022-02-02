from rest_framework import viewsets
from .models import Category, Logo, HeaderText
from .serializers import LogoSerializer, CategorySerializer, HeaderTextSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class LogoViewSet(viewsets.ViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer

    def list(self, request):
        self.queryset = Logo.objects.all()
        serializers_class = LogoSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        logo = get_object_or_404(self.queryset, slug=pk)
        serializers_class = LogoSerializer(logo)
        return Response(serializers_class.data)


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        self.queryset = Category.objects.all()
        serializers_class = CategorySerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(self.queryset, pk=pk)
        serializers_class = CategorySerializer(category)
        return Response(serializers_class.data)


class HeaderTextViewSet(viewsets.ViewSet):
    queryset = HeaderText.objects.all()
    serializer_class = HeaderTextSerializer

    def list(self, request):
        self.queryset = HeaderText.objects.all()
        serializers_class = HeaderTextSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(self.queryset, pk=pk)
        serializers_class = HeaderTextSerializer(category)
        return Response(serializers_class.data)