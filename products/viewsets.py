from rest_framework import viewsets
from .models import Category, Logo, HeaderText, SubSubCategory, SubCategory, Filter, Product, FAQ, UserMessage, Comment, DiscountProduct, Wishlist, Order, Subscriber
from .serializers import LogoSerializer, CategorySerializer, HeaderTextSerializer, SubCategorySerializer, SubSubCategorySerializer, FilterSerializer, ProductShowSerializer, FAQSerializer, UserMessageSerializer, CommentSerializer, DiscountProductSerializer, DiscountProductShowSerializer, WishlistShowSerializer, OrderSerializer, OrderShowSerializer, SubscriberSerializer, ProductUpdateSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .paginations import CustomPagination

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
        category = get_object_or_404(self.queryset, slug=pk)
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


class SubCategoryViewSet(viewsets.ViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def list(self, request):
        self.queryset = SubCategory.objects.all()
        serializers_class = SubCategorySerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(self.queryset, slug=pk)
        serializers_class = SubCategorySerializer(category)
        return Response(serializers_class.data)


class SubSubCategoryViewSet(viewsets.ViewSet):
    queryset = SubSubCategory.objects.all()
    serializer_class = SubSubCategorySerializer

    def list(self, request):
        self.queryset = SubSubCategory.objects.all()
        serializers_class = SubSubCategorySerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(self.queryset, slug=pk)
        serializers_class = SubSubCategorySerializer(category)
        return Response(serializers_class.data)


class FilterViewSet(viewsets.ViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer

    def list(self, request):
        self.queryset = Filter.objects.all()
        serializers_class = FilterSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        f = get_object_or_404(self.queryset, slug=pk)
        serializers_class = FilterSerializer(f)
        return Response(serializers_class.data)


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductShowSerializer
    # pagination_class = CustomPagination

    # def list(self, request):
    #     self.queryset = Product.objects.all()
    #     serializers_class = ProductShowSerializer(self.queryset, many=True)
    #     return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        f = get_object_or_404(self.queryset, pk=pk)
        views = f.views + 1
        f.update(views=views)
        serializers_class = ProductShowSerializer(f)
        return Response(serializers_class.data)


class ProductUpdateViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    # # pagination_class = CustomPagination

    # # def list(self, request):
    # #     self.queryset = Product.objects.all()
    # #     serializers_class = ProductShowSerializer(self.queryset, many=True)
    # #     return Response(serializers_class.data)

    # def retrieve(self, request, pk=None):
    #     f = get_object_or_404(self.queryset, pk=pk)
    #     serializers_class = ProductShowSerializer(f)
    #     return Response(serializers_class.data)


class FAQViewSet(viewsets.ViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request):
        self.queryset = FAQ.objects.all()
        serializers_class = FAQSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        faq = get_object_or_404(self.queryset, pk=pk)
        serializers_class = FAQSerializer(faq)
        return Response(serializers_class.data)


class UserMessageViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class DiscountProductViewSet(viewsets.ViewSet):
    queryset = DiscountProduct.objects.filter(is_verified=True)
    serializer_class = DiscountProductSerializer

    def retrieve(self, request, pk=None):
        discount_product = get_object_or_404(self.queryset, pk=pk)
        if discount_product.is_verified == True:
            serializers_class = DiscountProductShowSerializer(discount_product)
            return Response(serializers_class.data)
        return Response({"Detail": "No verified Products found."})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        self.queryset = Order.objects.all()
        serializers_class = OrderShowSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        order = get_object_or_404(self.queryset, pk=pk)
        serializers_class = OrderShowSerializer(order)
        return Response(serializers_class.data)


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def list(self, request):
        self.queryset = Subscriber.objects.all()
        serializers_class = SubscriberSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        subscriber = get_object_or_404(self.queryset, pk=pk)
        serializers_class = SubscriberSerializer(subscriber)
        return Response(serializers_class.data)