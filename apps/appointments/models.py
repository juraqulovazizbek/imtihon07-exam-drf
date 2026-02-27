from django.db import models
from django.conf import settings


class Appointment(models.Model):
    doctor = models.ForeignKey("doctors.DoctorProfile", on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timeslot = models.OneToOneField("doctors.TimeSlot", on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("cancelled", "Cancelled"),
        ],
        default="pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)