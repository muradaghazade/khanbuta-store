from django.urls import path, include
from accounts.views import RegisterUserAPI, MyObtainTokenPairView, GetUserDataByTokenView, VerifyNumberView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from accounts.viewsets import UserViewSet


app_name = "accounts"

router = DefaultRouter()

router.register('users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserAPI.as_view(), name='register'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-data/', GetUserDataByTokenView.as_view(), name='user-data'),
    path('verify-number/', VerifyNumberView.as_view(), name='verify-number'),
    
]