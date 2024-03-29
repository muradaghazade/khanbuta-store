from django.urls import path, include
from accounts.views import GetAllVendorsTwo, RegisterUserAPI, MyObtainTokenPairView, GetUserDataByTokenView, VerifyNumberView, AvenueByCityAPIView, AvenueByRegionAPIView, StreetByAvenueAPIView, UpdateUserView, CategoryBySubAPIView, CategoryBySubSubAPIView, GetAllStores, GetAllVendors, GetMixedStoresVendors, ResetPasswordAPIView, ResetPasswordTwoAPIView, ForgetPasswordAPIView, UserCategoryAPIView, RegionByCityAPIView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from accounts.viewsets import *


app_name = "accounts"

router = DefaultRouter()

router.register('users', UserViewSet, basename='user')
router.register('user-categories', UserCategoryViewSet, basename='user-category')
router.register('user-subcategories', UserSubCategoryViewSet, basename='user-sub')
router.register('user-subsubcategories', UserSubSubCategoryViewSet, basename='user-subsub')
router.register('cities', CityViewSet, basename='city')
router.register('regions', RegionViewSet, basename='region')
router.register('avenues', AvenueViewSet, basename='avenues')
router.register('streets', StreetViewSet, basename='street')
router.register('stores', StoreViewSet, basename='stores')
router.register('vendors', VendorViewSet, basename='vendors')
router.register('social-medias', SocialMediaViewSet, basename='social-media')
router.register('social-icons', SocialIconViewSet, basename='social-icon')


urlpatterns = [
    path('', include(router.urls)),
    path('categories/', UserCategoryAPIView.as_view(), name='category'),
    path('register/', RegisterUserAPI.as_view(), name='register'),
    path('stores/', GetAllStores.as_view(), name='store'),
    path('vendors/', GetAllVendors.as_view(), name='vendor'),
    path('stores-vendors/', GetMixedStoresVendors.as_view(), name='stores-vendors'),
    path('user/<int:pk>', UpdateUserView.as_view(), name='user'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-data/', GetUserDataByTokenView.as_view(), name='user-data'),
    path('verify-number/', VerifyNumberView.as_view(), name='verify-number'),
    path('sub-by-category/<int:id>/', CategoryBySubAPIView.as_view(), name='sub'),
    path('sub-by-subsub/<int:id>/', CategoryBySubSubAPIView.as_view(), name='sub-sub'),
    path('region-by-city/<int:pk>', RegionByCityAPIView.as_view(), name='region-by-city'),
    path('avenue-by-city/<int:pk>', AvenueByCityAPIView.as_view(), name='avenue-by-city'),
    path('avenue-by-region/<int:pk>', AvenueByRegionAPIView.as_view(), name='avenue-by-region'),
    path('street-by-avenue/<int:pk>', StreetByAvenueAPIView.as_view(), name='street-by-avenue'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),
    path('forgot-password/', ForgetPasswordAPIView.as_view(), name='forgot-password'),
    path('password-reset/', ResetPasswordTwoAPIView.as_view(), name='reset-password'),
]