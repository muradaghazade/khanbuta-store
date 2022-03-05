from rest_framework.routers import DefaultRouter
from .viewsets import LogoViewSet, CategoryViewSet, HeaderTextViewSet, SubCategoryViewSet, SubSubCategoryViewSet, FilterViewSet, ProductViewSet, FAQViewSet, UserMessageViewSet, CommentViewSet, DiscountProductViewSet, OrderViewSet
from .views import AboutUsAPIView, CategoryBySubAPIView, CategoryBySubSubAPIView, LastLogoAPIView, LastHeaderTextAPIView, FiltersBySubSubAPIView, CategoryLineAPI, NumberAPIView, RemoveFromWishlist, SliderAPIView, BenefitAPIView, DisplayedCategoryAPI, ProductCreateAPIView, ProductUpdateDeleteAPIView, ProductFilterAPIView, FAQView, ProductByUserView, RatingListCreateAPIView, AddToWishlist, RemoveFromWishlist, WishlistByUser, PartnerAPIView, ProductAPIView, CategoryBannerView, ProductVersionCreateAPIView, ProductByUserIDView, SearchAPIView, RemoveFromCart, DiscountProductCreateAPIView, DiscountProductsView, CartByUser
from django.urls import path, include

app_name = "products"

router = DefaultRouter()
router.register('logos', LogoViewSet, basename='logo')
router.register('orders', OrderViewSet, basename='order')
router.register('discounts', DiscountProductViewSet, basename='discount')
router.register('categories', CategoryViewSet, basename='category')
router.register('header-texts', HeaderTextViewSet, basename='header-text')
router.register('sub-categories', SubCategoryViewSet, basename='sub-category')
router.register('sub-sub-categories', SubSubCategoryViewSet, basename='sub-sub-category')
router.register('filters', FilterViewSet, basename='filter')
router.register('products', ProductViewSet, basename='products')
router.register('comments', CommentViewSet, basename='comments')
router.register('user-messages', UserMessageViewSet, basename='user-message')


urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/', ProductAPIView.as_view(), name='product'),
    path('discounts/', DiscountProductsView.as_view(), name='discounts'),
    path('discount-create/', DiscountProductCreateAPIView.as_view(), name='discount-create'),
    path('product-search/', SearchAPIView.as_view(), name='product-search'),
    path('user-cart/<int:id>/', CartByUser.as_view(), name='user-cart'),
    path('add-to-cart/', ProductVersionCreateAPIView.as_view(), name='product-version'),
    path('remove-from-cart/', RemoveFromCart.as_view(), name='remove-from-cart'),
    path('category-banner/', CategoryBannerView.as_view(), name='category-banner'),
    path('product-filter/', ProductFilterAPIView.as_view(), name='product-filter'),
    path('product/<int:pk>', ProductUpdateDeleteAPIView.as_view(), name='product-edit'),
    path('sub-by-category/<int:id>/', CategoryBySubAPIView.as_view(), name='sub'),
    path('category-line/', CategoryLineAPI.as_view(), name='category-line'),
    path('displayed-categories/', DisplayedCategoryAPI.as_view(), name='displayed-category'),
    path('sliders/', SliderAPIView.as_view(), name='slider'),
    path('benefits/', BenefitAPIView.as_view(), name='benefit'),
    path('partners/', PartnerAPIView.as_view(), name='partner'),
    path('sub-by-subsub/<int:id>/', CategoryBySubSubAPIView.as_view(), name='sub-sub'),
    path('logo/', LastLogoAPIView.as_view(), name='last-logo'),
    path('about-us/', AboutUsAPIView.as_view(), name='about-us'),
    path('header-text/', LastHeaderTextAPIView.as_view(), name='last-text'),
    path('filters-by-subsub/<int:id>/', FiltersBySubSubAPIView.as_view(), name='filter-sub'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('product-by-user/', ProductByUserView.as_view(), name='product-by-user'),
    path('product-by-user-id/<int:id>/', ProductByUserIDView.as_view(), name='product-by-user-id'),
    path('rating/',RatingListCreateAPIView.as_view(),name='rating-list'),
    path('add-to-wishlist/', AddToWishlist.as_view(),name='add-to-wishlist'),
    path('remove-from-wishlist/', RemoveFromWishlist.as_view(),name='remove-from-wishlist'),
    path('wishlist/<int:id>/', WishlistByUser.as_view(),name='wishlist'),
    path('number/', NumberAPIView.as_view(),name='number'),
]