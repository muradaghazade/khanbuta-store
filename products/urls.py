from rest_framework.routers import DefaultRouter
from .viewsets import LogoViewSet, CategoryViewSet, HeaderTextViewSet

app_name = "products"

router = DefaultRouter()
router.register('logos', LogoViewSet, basename='logo')
router.register('categories', CategoryViewSet, basename='category')
router.register('header-texts', HeaderTextViewSet, basename='header-text')
urlpatterns = router.urls