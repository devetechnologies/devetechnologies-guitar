from django.urls import path, include
from rest_framework.routers import DefaultRouter
from guitar.api.viewsets.guitar_viewsets import GuitarViewSet

# Create a router and register the GuitarViewSet
router = DefaultRouter()
router.register(r'guitar', GuitarViewSet,basename="guitar")

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = router.urls

