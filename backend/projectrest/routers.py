from rest_framework.routers import DefaultRouter
from product.viewset import ProductViewSet

router = DefaultRouter()

router.register('product-b', ProductViewSet, basename='product-a')
print(router.urls)

urlpatterns = router.urls