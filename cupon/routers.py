from rest_framework.routers import DefaultRouter
from .views import CuponViewSet

router = DefaultRouter()

router.register('', CuponViewSet, basename='cupon')

urlpatterns = router.urls