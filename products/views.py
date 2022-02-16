from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Category, SubCategory, SubSubCategory, Logo, HeaderText, Filter, CategoryLine, Slider, Benefit, DisplayedCategory, Product, Image, FilterValue
from .serializers import CategoryLineSerializer, FilterSerializer, SubCategorySerializer, SubSubCategorySerializer, LogoSerializer, HeaderTextSerializer, FilterSerializer, SliderSerializer, BenefitSerializer, ProductSerializer, ImageSerializer


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


class ProductCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        images = request.data["images"]
        filter_values = request.data["filter_values"]
        product = Product.objects.create(title=request.data["title"],description=request.data["description"],price=request.data["price"],short_desc1=request.data["short_desc1"],short_desc2=request.data["short_desc2"],short_desc3=request.data["short_desc3"],main_image=request.data["main_image"],user=request.user)
        Image.objects.bulk_create(
            [Image(image=i, product=product) for i in images]
        )
        FilterValue.objects.bulk_create(
            [FilterValue(value=i["value"], the_filter=Filter.objects.get(pk=i["filter"]), product=product) for i in filter_values]
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductUpdateDeleteAPIView(APIView):
    def patch(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductSerializer(product).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        course = get_object_or_404(Product, pk=kwargs['id'])
        course.delete()
        return Response("Product deleted", status=status.HTTP_204_NO_CONTENT)