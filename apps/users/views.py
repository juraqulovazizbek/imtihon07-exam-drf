from rest_framework.viewsets import ModelViewSet
from .models import User, PatientProfile
from .serializers import UserSerializer, PatientProfileSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PatientProfileViewSet(ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer