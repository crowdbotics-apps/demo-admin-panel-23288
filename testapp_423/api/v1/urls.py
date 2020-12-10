from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AaaViewSet

router = DefaultRouter()
router.register("aaa", AaaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
