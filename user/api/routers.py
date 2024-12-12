from django.db import router
from rest_framework.routers import DefaultRouter
from user.api.viewsets.user_viewsets import *

router = DefaultRouter()

router.register(r'user', UserViewSet,
                basename="user")

urlpatterns = router.urls