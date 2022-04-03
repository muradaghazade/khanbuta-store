from rest_framework import serializers
from .models import *
from accounts.seralizers import UserCategorySerializer, CitySerializer, RegionSerializer, AvenueSerializer, StreetSerializer
from accounts.seralizers import UserSerializer, UserShowSerializer
from drf_extra_fields.fields import Base64ImageField


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ('id', 'title', 'image', 'created_at', 'updated_at')


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'title', 'description', 'image', 'button_text', 'button_link')


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


class CategoryReklamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryReklam
        fields = ('id','title','image','created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, required=False)
    category_reklam = CategoryReklamSerializer(required=False)
    class Meta:
        model = Category
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at', 'sub_categories', 'category_reklam')


class CategoryLineSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    class Meta:
        model = Category
        fields = ('id', 'category')


class DisplayedCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    class Meta:
        model = DisplayedCategory
        fields = ('id', 'category', 'image')


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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'email', 'review', 'product')

class ProductShowSerializer(serializers.ModelSerializer):
    main_image = Base64ImageField(required=False)
    sub_sub_category = SubSubCategorySerializer(required=False)
    sub_category = SubCategorySerializer(required=False)
    category = CategorySerializer(required=False)
    images = ImageSerializer(many=True, required=False)
    filter_values = FilterValueShowSerializer(many=True, required=False)
    tag = TagSerializer(many=True, required=False)
    comments = CommentSerializer(many=True, required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'code', 'price', 'short_desc1', 'short_desc2', 'short_desc3', 'main_image','rating', 'comments', 'sub_sub_category', 'sub_category', 'category', 'user', 'images', 'filter_values', 'tag', 'created_at', 'updated_at')


class ProductSerializer(serializers.ModelSerializer):
    main_image = Base64ImageField(required=False)
    # sub_sub_category = SubSubCategorySerializer(required=False)
    # sub_category = SubCategorySerializer(required=False)
    # category = CategorySerializer(required=False)
    images = ImageSerializer(many=True, required=False)
    filter_values = FilterValueSerializer(many=True, required=False)
    tag = TagSerializer(many=True, required=False)
    # user = UserSerializer(required=False)
    

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'short_desc1', 'short_desc2', 'short_desc3',  'main_image', 'sub_sub_category', 'images', 'filter_values', 'tag', 'category', 'sub_category','sub_sub_category', 'user', 'created_at', 'updated_at')

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
            sub_sub_category = validated_data['sub_sub_category'],
            category = validated_data['category'],
            sub_category = validated_data['sub_category'],
            user = validated_data['user'],

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


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('author','product','rating')
        read_only_fields = ('author',)


class DiscountProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountProduct
        fields = ('id','discount_price','product','time_range')


class DiscountProductShowSerializer(serializers.ModelSerializer):
    product = ProductShowSerializer(required=False)
    class Meta:
        model = DiscountProduct
        fields = ('id','discount_price','product','time_range')


class WishlistShowSerializer(serializers.ModelSerializer):
    product = ProductShowSerializer(required=False, many=True)
    user = UserSerializer(required=False)
    class Meta:
        model = Wishlist
        fields = ('id','user', 'product', 'created_at', 'updated_at')


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id','title','logo')


class CategoryBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryBanner
        fields = ('id', 'image', 'button_text', 'button_link', 'created_at', 'updated_at')


class ProductVersionSerializer(serializers.ModelSerializer):
    # product = ProductShowSerializer(required=False)
    class Meta:
        model = ProductVersion
        fields = ('id', 'final_price', 'quantity', 'product', 'created_at', 'updated_at')


class ProductVersionShowSerializer(serializers.ModelSerializer):
    product = ProductShowSerializer(required=False)
    class Meta:
        model = ProductVersion
        fields = ('id', 'final_price', 'quantity', 'product', 'created_at', 'updated_at')


class CartShowSerializer(serializers.ModelSerializer):
    product_version = ProductVersionShowSerializer(required=False, many=True)
    user = UserSerializer(required=False)
    class Meta:
        model = Cart
        fields = ('id','user', 'product_version', 'created_at', 'updated_at')


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ('id', 'number', 'created_at', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'first_name', 'last_name', 'address', 'zip_code', 'email', 'number', 'order_notes', 'cart', 'status', 'buyer', 'company_name', 'created_at', 'updated_at')


class OrderShowSerializer(serializers.ModelSerializer):
    cart = CartShowSerializer(required=False)
    buyer = UserShowSerializer(required=False)
    class Meta:
        model = Order
        fields = ('id', 'first_name', 'last_name', 'address', 'zip_code', 'email', 'number', 'order_notes', 'cart', 'status', 'buyer', 'company_name', 'created_at', 'updated_at')


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('id', 'email', 'created_at', 'updated_at')


class StoreOrderSerializer(serializers.ModelSerializer):
    store = UserSerializer(required=False)
    product_versions = ProductVersionShowSerializer(required=False, many=True)
    class Meta:
        model = StoreOrder
        fields = ('id', 'first_name', 'last_name', 'company_name', 'address', 'zip_code', 'email', 'number', 'order_notes', 'status', 'store', 'product_versions', 'created_at', 'updated_at')


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ('id', 'title', 'url', 'logo', 'created_at', 'updated_at')


class VendorSerializer(serializers.ModelSerializer):
    category = UserCategorySerializer(required=False)
    products = ProductShowSerializer(required=False, many=True)
    city = CitySerializer(required=False)
    region = RegionSerializer(required=False)
    avenue = AvenueSerializer(required=False)
    class Meta:
        model = User
        fields = ('id', 'number', 'name', 'is_vendor', 'is_verified_by_admin', 'email', 'rating', 'city', 'region', 'avenue', 'street', 'address_addtional', 'cover_image', 'logo', 'category', 'products')