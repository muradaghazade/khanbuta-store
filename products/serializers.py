from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import Base64ImageField


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ('id', 'title', 'image', 'created_at', 'updated_at')


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'title', 'description', 'image')


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ('id', 'title', 'description', 'icon')


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


class CategoryLineSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    class Meta:
        model = Category
        fields = ('id', 'category')


class HeaderTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderText
        fields = ('id', 'content', 'created_at', 'updated_at')


class FilterSerializer(serializers.ModelSerializer):
    sub_sub_category = SubSubCategorySerializer(required=False)
    class Meta:
        model = Filter
        fields = ('id', 'title', 'created_at', 'updated_at', 'sub_sub_category')


class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = Image
        fields = ('id', 'image', 'created_at', 'updated_at' )


class FilterValueSerializer(serializers.ModelSerializer):
    the_filter = FilterSerializer(required=False)
    class Meta:
        model = FilterValue
        fields = ('id', 'value', 'the_filter')


class ProductSerializer(serializers.ModelSerializer):
    sub_sub_category = SubSubCategorySerializer(required=False)
    images = ImageSerializer(many=True, required=False)
    filter_values = FilterValueSerializer(many=True, required=False)
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'short_desc1', 'short_desc2', 'short_desc3', 'main_image', 'sub_sub_category', 'images', 'filter_values', 'created_at', 'updated_at')