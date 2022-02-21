from traceback import print_tb
from rest_framework import serializers
from .models import *
from accounts.seralizers import UserSerializer
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
    # the_filter = FilterSerializer(required=False)
    class Meta:
        model = FilterValue
        fields = ('id', 'value', 'the_filter')


class FilterValueShowSerializer(serializers.ModelSerializer):
    the_filter = FilterSerializer(required=False)
    class Meta:
        model = FilterValue
        fields = ('id', 'value', 'the_filter')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title', 'created_at', 'updated_at')


class ProductShowSerializer(serializers.ModelSerializer):
    main_image = Base64ImageField(required=False)
    sub_sub_category = SubSubCategorySerializer(required=False)
    images = ImageSerializer(many=True, required=False)
    filter_values = FilterValueShowSerializer(many=True, required=False)
    tag = TagSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'short_desc1', 'short_desc2', 'short_desc3', 'main_image', 'sub_sub_category', 'images', 'filter_values', 'tag', 'created_at', 'updated_at')


class ProductSerializer(serializers.ModelSerializer):
    main_image = Base64ImageField(required=False)
    sub_sub_category = SubSubCategorySerializer(required=False)
    images = ImageSerializer(many=True, required=False)
    filter_values = FilterValueSerializer(many=True, required=False)
    tag = TagSerializer(many=True, required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'short_desc1', 'short_desc2', 'short_desc3', 'main_image', 'sub_sub_category', 'images', 'filter_values', 'tag', 'user', 'created_at', 'updated_at')

    def create(self, validated_data):
        print(validated_data['tag'])
        product = Product.objects.create(
            title = validated_data['title'],
            description = validated_data['description'],
            price = validated_data['price'],
            short_desc1 = validated_data['short_desc1'],
            short_desc2 = validated_data['short_desc2'],
            short_desc3 = validated_data['short_desc3'],
            main_image = validated_data['main_image'],

        )

        #images
        for i in validated_data['images']:
            image = Image(image=i['image'], product=product)
            image.save()
            product.images.add(image)

        #filter
        for i in validated_data['filter_values']:
            f = FilterValue(value=i["value"], the_filter=i["the_filter"], product=product)
            f.save()

        #tags
        for i in validated_data['tag']:
            t = Tag(title=i['title'])
            t.save()
            product.tag.add(t)
        product.save()
        return product


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer')


class AboutUsServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsService
        fields = ('id', 'title', 'description')


class AboutUsCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsCarousel
        fields = ('id', 'title', 'amount', 'description')


class AboutUsSerializer(serializers.ModelSerializer):
    corousel = AboutUsCarouselSerializer(many=True, required=False)
    services = AboutUsServiceSerializer(many=True, required=False)
    class Meta:
        model = AboutUs
        fields = ('id', 'content', 'service_title', 'service_image', 'services', 'corousel', 'banner_title', 'banner_text', 'banner_button_text', 'banner_button_link',)

    
class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = ('id', 'name', 'email', 'message')


class FAQCategorySerializer(serializers.ModelSerializer):
    faqs = FAQSerializer(many=True, required=False)
    class Meta:
        model = FAQCategory
        fields = ('id', 'title', 'faqs')