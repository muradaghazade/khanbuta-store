from django.urls import path, include
from accounts.views import RegisterUserAPI, MyObtainTokenPairView, GetUserDataByTokenView, VerifyNumberView, AvenueByCityAPIView, AvenueByRegionAPIView, StreetByAvenueAPIView, UpdateUserView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from accounts.viewsets import *


app_name = "accounts"

router = DefaultRouter()

router.register('users', UserViewSet, basename='user')
router.register('cities', CityViewSet, basename='city')
router.register('regions', RegionViewSet, basename='region')
router.register('avenues', AvenueViewSet, basename='avenues')
router.register('streets', StreetViewSet, basename='street')
router.register('social-medias', SocialMediaViewSet, basename='social-media')
router.register('social-icons', SocialIconViewSet, basename='social-icon')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserAPI.as_view(), name='register'),
    path('user/<int:pk>', UpdateUserView.as_view(), name='user'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-data/', GetUserDataByTokenView.as_view(), name='user-data'),
    path('verify-number/', VerifyNumberView.as_view(), name='verify-number'),
    path('avenue-by-city/<int:pk>', AvenueByCityAPIView.as_view(), name='avenue-by-city'),
    path('avenue-by-region/<int:pk>', AvenueByRegionAPIView.as_view(), name='avenue-by-region'),
    path('street-by-avenue/<int:pk>', StreetByAvenueAPIView.as_view(), name='street-by-avenue'),
    
]