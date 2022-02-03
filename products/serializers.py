from rest_framework import serializers
from .models import *


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ('id', 'title', 'image', 'created_at', 'updated_at')


class SubSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSubCategory
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at')


class SubCategorySerializer(serializers.ModelSerializer):
    sub_sub_categories = SubSubCategorySerializer(many=True, required=False)
    class Meta:
        model = SubCategory
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at', 'sub_sub_categories')


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, required=False)
    class Meta:
        model = Category
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at', 'sub_categories')


class HeaderTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderText
        fields = ('id', 'content', 'created_at', 'updated_at')