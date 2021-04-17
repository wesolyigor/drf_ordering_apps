from rest_framework.routers import SimpleRouter

from api import views

router = SimpleRouter()
router.register('offer', views.OfferViewSet, basename='offer')
router.register('category', views.CategoryViewSet, basename='category')

urlpatterns = router.urls