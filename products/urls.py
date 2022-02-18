from rest_framework.routers import DefaultRouter
from .viewsets import LogoViewSet, CategoryViewSet, HeaderTextViewSet, SubCategoryViewSet, SubSubCategoryViewSet, FilterViewSet, ProductViewSet, FAQViewSet
from .views import CategoryBySubAPIView, CategoryBySubSubAPIView, LastLogoAPIView, LastHeaderTextAPIView, FiltersBySubSubAPIView, CategoryLineAPI, SliderAPIView, BenefitAPIView, DisplayedCategoryAPI, ProductCreateAPIView, ProductUpdateDeleteAPIView
from django.urls import path, include

app_name = "products"

router = DefaultRouter()
router.register('logos', LogoViewSet, basename='logo')
router.register('categories', CategoryViewSet, basename='category')
router.register('header-texts', HeaderTextViewSet, basename='header-text')
router.register('sub-categories', SubCategoryViewSet, basename='sub-category')
router.register('sub-sub-categories', SubSubCategoryViewSet, basename='sub-sub-category')
router.register('filters', FilterViewSet, basename='filter')
router.register('products', ProductViewSet, basename='products')
router.register('faq', FAQViewSet, basename='faq')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductCreateAPIView.as_view(), name='product-create'),
    path('product/<int:pk>', ProductUpdateDeleteAPIView.as_view(), name='product-edit'),
    path('categories/<slug:slug>/<slug:slug2>/', CategoryBySubAPIView.as_view(), name='sub'),
    path('category-line/', CategoryLineAPI.as_view(), name='category-line'),
    path('displayed-categories/', DisplayedCategoryAPI.as_view(), name='displayed-category'),
    path('sliders/', SliderAPIView.as_view(), name='slider'),
    path('benefits/', BenefitAPIView.as_view(), name='benefit'),
    path('categories/<slug:slug>/<slug:slug2>/<slug:slug3>/', CategoryBySubSubAPIView.as_view(), name='sub-sub'),
    path('logo/', LastLogoAPIView.as_view(), name='last-logo'),
    path('header-text/', LastHeaderTextAPIView.as_view(), name='last-text'),
    path('filters-by-subsub/<int:id>/', FiltersBySubSubAPIView.as_view(), name='filter-sub'),
]