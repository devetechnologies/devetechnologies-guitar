from django.db import router
from rest_framework.routers import DefaultRouter
from user.api.viewsets.user_viewsets import *

router = DefaultRouter()

router.register('user-list', UserViewSet,
                basename="user-list")

urlpatterns = router.urls