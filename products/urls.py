from rest_framework.routers import DefaultRouter
from .viewsets import LogoViewSet, CategoryViewSet, HeaderTextViewSet, SubCategoryViewSet, SubSubCategoryViewSet, FilterViewSet, ProductViewSet, FAQViewSet, UserMessageViewSet, CommentViewSet, DiscountProductViewSet
from .views import AboutUsAPIView, CategoryBySubAPIView, CategoryBySubSubAPIView, LastLogoAPIView, LastHeaderTextAPIView, FiltersBySubSubAPIView, CategoryLineAPI, SliderAPIView, BenefitAPIView, DisplayedCategoryAPI, ProductCreateAPIView, ProductUpdateDeleteAPIView, ProductFilterAPIView, FAQView, ProductByUserView, RatingListCreateAPIView
from django.urls import path, include

app_name = "products"

router = DefaultRouter()
router.register('logos', LogoViewSet, basename='logo')
router.register('discounts', DiscountProductViewSet, basename='discount')
router.register('categories', CategoryViewSet, basename='category')
router.register('header-texts', HeaderTextViewSet, basename='header-text')
router.register('sub-categories', SubCategoryViewSet, basename='sub-category')
router.register('sub-sub-categories', SubSubCategoryViewSet, basename='sub-sub-category')
router.register('filters', FilterViewSet, basename='filter')
router.register('products', ProductViewSet, basename='products')
router.register('comments', CommentViewSet, basename='comments')
router.register('user-messages', UserMessageViewSet, basename='user-message')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductCreateAPIView.as_view(), name='product-create'),
    path('product-filter/', ProductFilterAPIView.as_view(), name='product-filter'),
    path('product/<int:pk>', ProductUpdateDeleteAPIView.as_view(), name='product-edit'),
    path('categories/<slug:slug>/<slug:slug2>/', CategoryBySubAPIView.as_view(), name='sub'),
    path('category-line/', CategoryLineAPI.as_view(), name='category-line'),
    path('displayed-categories/', DisplayedCategoryAPI.as_view(), name='displayed-category'),
    path('sliders/', SliderAPIView.as_view(), name='slider'),
    path('benefits/', BenefitAPIView.as_view(), name='benefit'),
    path('categories/<slug:slug>/<slug:slug2>/<slug:slug3>/', CategoryBySubSubAPIView.as_view(), name='sub-sub'),
    path('logo/', LastLogoAPIView.as_view(), name='last-logo'),
    path('about-us/', AboutUsAPIView.as_view(), name='about-us'),
    path('header-text/', LastHeaderTextAPIView.as_view(), name='last-text'),
    path('filters-by-subsub/<int:id>/', FiltersBySubSubAPIView.as_view(), name='filter-sub'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('product-by-user/', ProductByUserView.as_view(), name='product-by-user'),
    path('rating/',RatingListCreateAPIView.as_view(),name='rating-list'),
]