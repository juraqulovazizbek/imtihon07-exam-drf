from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorProfileViewSet, TimeSlotViewSet

router = DefaultRouter()
router.register("doctors", DoctorProfileViewSet, basename="doctors")
router.register("timeslots", TimeSlotViewSet, basename="timeslots")

urlpatterns = [
    path("", include(router.urls)),
]