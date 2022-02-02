from rest_framework import serializers
from .models import Logo, HeaderText, Category


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ('id', 'title', 'image', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at')


class HeaderTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderText
        fields = ('id', 'content', 'created_at', 'updated_at')