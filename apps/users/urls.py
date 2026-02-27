from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PatientProfileViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("patients", PatientProfileViewSet, basename="patients")

urlpatterns = [
    path("", include(router.urls)),
]