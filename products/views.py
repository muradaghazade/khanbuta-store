from math import floor
from urllib import request
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import AboutUs, Cart, Category, FAQCategory, SubCategory, SubSubCategory, Logo, HeaderText, Filter, CategoryLine, Slider, Benefit, DisplayedCategory, Product, Image, FilterValue, Tag, Rating, Wishlist, Partner, ProductVersion, CategoryBanner, DiscountProduct, Number, StoreOrder, SocialLink, CategoryReklam, Order
from .serializers import CategoryLineSerializer, FAQCategorySerializer, FilterSerializer, SubCategorySerializer, SubSubCategorySerializer, LogoSerializer, HeaderTextSerializer, FilterSerializer, SliderSerializer, BenefitSerializer, ProductSerializer, ImageSerializer, AboutUsSerializer, RatingSerializer, WishlistShowSerializer, PartnerSerializer, ProductShowSerializer, CategoryBannerSerializer, ProductVersionSerializer, DiscountProductSerializer, DiscountProductShowSerializer, NumberSerializer, CartShowSerializer, StoreOrderSerializer, SocialLinkSerializer, DisplayedCategorySerializer, CategoryReklamSerializer, OrderShowSerializer
from django.db.models import Q
from accounts.models import User
from .paginations import CustomPagination


class OrderByBuyerAPIView(APIView):
    def get(self, request, *args, **kwargs):
        street = Order.objects.filter(buyer__pk=kwargs['pk'])
        serializer = OrderShowSerializer(street, many=True)
        return Response(serializer.data)


class FilterPricesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        price_list = []
        products = Product.objects.all()
        for product in products:
            price_list.append(product.price)
        mini = floor(min(price_list))
        maxi = floor(max(price_list))
        ranges = [[i, i+5] for i in range(mini,maxi,maxi//5)]
        print(ranges)
        return Response(ranges)


class SocialLinkAPIView(ListAPIView):
    model = SocialLink
    serializer_class = SocialLinkSerializer
    queryset = SocialLink.objects.order_by('-id')


class StoreOrderAPIView(ListAPIView):
    model = StoreOrder
    serializer_class = StoreOrderSerializer
    pagination_class = CustomPagination
    queryset = StoreOrder.objects.order_by('-id')

    def get_queryset(self):
        print(self.request.data)
        queryset = StoreOrder.objects.order_by('-id')
        id = self.request.data.get('id')

        if id:
            queryset = queryset.filter(store__id=id)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SearchAPIView(ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    queryset = Product.objects.order_by('-id')

    def get_queryset(self):
        print(self.request.data)
        queryset = Product.objects.order_by('-id')
        title = self.request.data.get('title')

        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductAPIView(ListAPIView):
    model = Product
    serializer_class = ProductShowSerializer
    pagination_class = CustomPagination
    queryset = Product.objects.order_by('-id')

    def get_queryset(self):
        print(self.request.data)
        queryset = Product.objects.order_by('-id')
        az = self.request.data.get('az')
        za = self.request.data.get('za')
        expensive = self.request.data.get('expensive')
        cheap = self.request.data.get('cheap')

        if az:
            queryset = queryset.order_by('title')

        if za:
            queryset = queryset.order_by('-title')

        if expensive:
            queryset = queryset.order_by('-price')

        if cheap:
            queryset = queryset.order_by('price')
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductByUserView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.user)
        products = Product.objects.filter(user=request.user)
        # category = get_object_or_404(SubCategory, category__slug=kwargs['slug'], slug=kwargs['slug2'])
        serializer = ProductShowSerializer(products, many=True)
        return Response(serializer.data)


class ProductByUserIDView(APIView):
    def get(self, request, *args, **kwargs):
        # print(request.user)
        print(request.data.get('category'))
        products = Product.objects.filter(user__id=kwargs['id'])
        # category = get_object_or_404(SubCategory, category__slug=kwargs['slug'], slug=kwargs['slug2'])
        serializer = ProductShowSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data.get('category'))
        queryset = Product.objects.filter(user__id=kwargs['id'])
        az = self.request.data.get('az')
        za = self.request.data.get('za')
        expensive = self.request.data.get('expensive')
        cheap = self.request.data.get('cheap')
        category = self.request.data.get('category')
        sub_category = self.request.data.get('sub_category')
        sub_sub_category = self.request.data.get('sub_sub_category')
        brand = self.request.data.get('brand')
        price_list = self.request.data.get('price')

        if az:
            queryset = queryset.order_by('title')

        if za:
            queryset = queryset.order_by('-title')

        if expensive:
            queryset = queryset.order_by('-price')

        if cheap:
            queryset = queryset.order_by('price')

        if category:
            queryset = queryset.filter(category__title__icontains=category)

        if sub_category:
            queryset = queryset.filter(sub_category__title__icontains=sub_category)

        if sub_sub_category:
            queryset = queryset.filter(sub_sub_category__title__in=sub_sub_category)

        if brand:
            queryset = queryset.filter(brand__icontains=brand)

        if price_list:
            queries = Q()
            for price in price_list:
                queries = Q(price__range=(price)) | queries
            
            queryset = queryset.filter(queries)
        # category = get_object_or_404(SubCategory, category__slug=kwargs['slug'], slug=kwargs['slug2'])
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)    


class ProductFilterAPIView(ListAPIView):
    model = Product
    serializer_class = ProductShowSerializer
    pagination_class = CustomPagination
    queryset = Product.objects.order_by('-id')

    def get_queryset(self):
        print(self.request.data)
        print(self.request.data.get('category'))
        category = self.request.data.get('category')
        sub_category = self.request.data.get('sub_category')
        sub_sub_category = self.request.data.get('sub_sub_category')
        brand = self.request.data.get('brand')
        price_list = self.request.data.get('price')
        queryset = Product.objects.all()
        if category:
            queryset = queryset.filter(category__title__icontains=category)

        if sub_category:
            queryset = queryset.filter(sub_category__title__icontains=sub_category)

        if sub_sub_category:
            queryset = queryset.filter(sub_sub_category__title__in=sub_sub_category)

        if brand:
            queryset = queryset.filter(brand__icontains=brand)

        if price_list:
            queries = Q()
            for price in price_list:
                queries = Q(price__range=(price)) | queries
            
            queryset = queryset.filter(queries)
        
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RatingListCreateAPIView(ListCreateAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        rat = Rating.objects.filter(product=product, author=self.request.user).first()
        if not rat:
            serializer.validated_data['author'] = self.request.user
            serializer.save()
        else:
            rat.rating = serializer.validated_data['rating']
            rat.save()


class BenefitAPIView(ListAPIView):
    model = Benefit
    serializer_class = BenefitSerializer
    queryset = Benefit.objects.all()


class PartnerAPIView(ListAPIView):
    model = Partner
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class SliderAPIView(ListAPIView):
    model = Slider
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()


class CategoryLineAPI(ListAPIView):
    model = CategoryLine
    serializer_class = CategoryLineSerializer
    queryset = CategoryLine.objects.all()


class DisplayedCategoryAPI(ListAPIView):
    model = DisplayedCategory
    serializer_class = DisplayedCategorySerializer
    queryset = DisplayedCategory.objects.all()


class CategoryBySubAPIView(APIView):
    def post(self, request, *args, **kwargs):
        category = SubCategory.objects.filter(category__id=self.request.data.get('id'))
        serializer = SubCategorySerializer(category, many=True)
        return Response(serializer.data)
       

class CategoryBySubSubAPIView(APIView):
    def post(self, request, *args, **kwargs):
        category = SubSubCategory.objects.filter(category__id=self.request.data.get('id'))
        serializer = SubSubCategorySerializer(category, many=True)
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


class ProductCreateAPIView(CreateAPIView):
    model = Product
    serializer_class = ProductSerializer

    # def perform_create(self, serializer):
    #     print(self.request.user)
    #     product_version = serializer.save(user=self.request.user)


class ProductUpdateDeleteAPIView(APIView):
    def patch(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductSerializer(product).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        product.delete()
        return Response("Product deleted", status=status.HTTP_204_NO_CONTENT)


class AboutUsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        aboutus = AboutUs.objects.order_by("-id").first()
        serializer = AboutUsSerializer(aboutus)
        return Response(serializer.data)


class FAQView(ListAPIView):
    model = FAQCategory
    serializer_class = FAQCategorySerializer
    queryset = FAQCategory.objects.all()


# class CategoryReklamAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         # category = get_object_or_404(Product, category__id=kwargs['id'])
#         category = CategoryReklam.objects.filter(category__id=kwargs['id']).first()
#         serializer = CategoryReklamSerializer(category)
#         return Response(serializer.data)


class AddToWishlist(APIView):
    def post(self, request, *args, **kwargs):
        product_id = self.request.data.get('product')
        user_id = self.request.data.get('user')
        product = get_object_or_404(Product, pk=int(product_id))
        user = get_object_or_404(User, pk=int(user_id))
        user.wishlist.product.add(product)
        return Response("Added to Wishlist")


class RemoveFromWishlist(APIView):
    def post(self, request, *args, **kwargs):
        product_id = self.request.data.get('product')
        user_id = self.request.data.get('user')
        product = get_object_or_404(Product, pk=int(product_id))
        user = get_object_or_404(User, pk=int(user_id))
        user.wishlist.product.remove(product)
        return Response("Removed from Wishlist")


class WishlistByUser(APIView):
    def get(self, request, *args, **kwargs):
        f = Wishlist.objects.filter(user__id=kwargs['id']).first()
        serializer = WishlistShowSerializer(f)
        return Response(serializer.data)


class RemoveFromCart(APIView):
    def post(self, request, *args, **kwargs):
        product_id = self.request.data.get('product')
        user_id = self.request.data.get('user')
        product = get_object_or_404(ProductVersion, pk=int(product_id))
        user = get_object_or_404(User, pk=int(user_id))
        user.user_cart.product_version.remove(product)
        return Response("Removed from Cart")


class CategoryBannerView(APIView):
    def get(self, request, *args, **kwargs):
        f = CategoryBanner.objects.order_by('-id').first()
        serializer = CategoryBannerSerializer(f)
        return Response(serializer.data)


class ProductVersionCreateAPIView(CreateAPIView):
    model = ProductVersion
    serializer_class = ProductVersionSerializer
    # permission_class = IsAuthenticated

    def perform_create(self, serializer):
        product_version = serializer.save()
        user = self.request.user
        user.user_cart.product_version.add(product_version)
        # Wishlist.objects.create(user=user)


class CartByUser(APIView):
    def get(self, request, *args, **kwargs):
        f = Cart.objects.filter(user__id=kwargs['id']).first()
        serializer = CartShowSerializer(f)
        return Response(serializer.data)


class DiscountProductCreateAPIView(CreateAPIView):
    model = DiscountProduct
    serializer_class = DiscountProductSerializer


class DiscountProductsView(ListAPIView):
    model = DiscountProduct
    serializer_class = DiscountProductShowSerializer
    pagination_class = CustomPagination
    queryset = DiscountProduct.objects.order_by('-id')

    def get_queryset(self):
        print(self.request.data)
        queryset = DiscountProduct.objects.order_by('-id')
        title = self.request.data.get('title')
        category = self.request.data.get('category')
        sub_category = self.request.data.get('sub_category')
        sub_sub_category = self.request.data.get('sub_sub_category')
        brand = self.request.data.get('brand')
        price_list = self.request.data.get('price')

        if title:
            queryset = queryset.filter(product__title__icontains=title)

        if category:
            queryset = queryset.filter(product__category__title__icontains=category)

        if sub_category:
            queryset = queryset.filter(product__sub_category__title__icontains=sub_category)

        if sub_sub_category:
            queryset = queryset.filter(product__sub_sub_category__title__in=sub_sub_category)

        if brand:
            queryset = queryset.filter(product__brand__icontains=brand)

        if price_list:
            queries = Q()
            for price in price_list:
                queries = Q(price__range=(price)) | queries
            
            queryset = queryset.filter(queries)

        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NumberAPIView(APIView):
    def get(self, request, *args, **kwargs):
        number = Number.objects.order_by("-id").first()
        serializer = NumberSerializer(number)
        return Response(serializer.data)