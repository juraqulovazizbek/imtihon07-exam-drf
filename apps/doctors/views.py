from rest_framework.viewsets import ModelViewSet
from .models import DoctorProfile, TimeSlot
from .serializers import DoctorProfileSerializer, TimeSlotSerializer


class DoctorProfileViewSet(ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer


class TimeSlotViewSet(ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer