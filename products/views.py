from pyexpat import model
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import AboutUs, Category, FAQCategory, SubCategory, SubSubCategory, Logo, HeaderText, Filter, CategoryLine, Slider, Benefit, DisplayedCategory, Product, Image, FilterValue, Tag, Rating
from .serializers import CategoryLineSerializer, FAQCategorySerializer, FilterSerializer, SubCategorySerializer, SubSubCategorySerializer, LogoSerializer, HeaderTextSerializer, FilterSerializer, SliderSerializer, BenefitSerializer, ProductSerializer, ImageSerializer, AboutUsSerializer, RatingSerializer
from django.db.models import Q


class ProductByUserView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.user)
        products = Product.objects.filter(user=request.user)
        # category = get_object_or_404(SubCategory, category__slug=kwargs['slug'], slug=kwargs['slug2'])
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductFilterAPIView(ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        category = self.request.data.get('category')
        brand = self.request.data.get('brand')
        price_list = self.request.data.get('price')
        queryset = Product.objects.all()
        if category:
            queryset = queryset.filter(sub_sub_category__title__icontains=category)

        if brand:
            queryset = queryset.filter(brand__icontains=brand)

        if price_list:
            queries = Q()
            for price in price_list:
                queries = Q(price__range=(price)) | queries
            
            queryset = queryset.filter(queries)
        
        return queryset


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
    serializer_class = CategoryLineSerializer
    queryset = DisplayedCategory.objects.all()


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


class ProductCreateAPIView(CreateAPIView):
    model = Product
    serializer_class = ProductSerializer


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
