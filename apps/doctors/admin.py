from django.contrib import admin
from .models import DoctorProfile, TimeSlot

admin.site.register(DoctorProfile)
admin.site.register(TimeSlot)