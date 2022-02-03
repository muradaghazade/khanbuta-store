from rest_framework.routers import DefaultRouter
from .viewsets import LogoViewSet, CategoryViewSet, HeaderTextViewSet, SubCategoryViewSet, SubSubCategoryViewSet
from .views import CategoryBySubAPIView, CategoryBySubSubAPIView
from django.urls import path, include

app_name = "products"

router = DefaultRouter()
router.register('logos', LogoViewSet, basename='logo')
router.register('categories', CategoryViewSet, basename='category')
router.register('header-texts', HeaderTextViewSet, basename='header-text')
router.register('sub-categories', SubCategoryViewSet, basename='sub-category')
router.register('sub-sub-categories', SubSubCategoryViewSet, basename='sub-sub-category')
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('categories/<slug:slug>/<slug:slug2>', CategoryBySubAPIView.as_view(), name='sub'),
    path('categories/<slug:slug>/<slug:slug2>/<slug:slug3>', CategoryBySubSubAPIView.as_view(), name='sub-sub'),
]