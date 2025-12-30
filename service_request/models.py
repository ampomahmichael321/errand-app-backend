from django.db import models
from django.utils import timezone

# Create your models here.
class ServiceRequest(models.Model):
    username = models.CharField(max_length=250)
    user_email = models.EmailField()
    user_phone = models.PositiveBigIntegerField(max_length=10)
    service_type = models.CharField(max_length=10)
    pickup_location = models.CharField(max_length=250, null=True, blank=True)
    dropoff_location = models.CharField(max_length=250, null=True, blank=True)
    delivery_location = models.CharField(max_length=250, null=True, blank=True)
    errand_destination = models.CharField(max_length=250, null=True, blank=True)
    request_details = models.TextField()
    additional_info = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now,)
    status = models.CharField(max_length=20, default='pending')
    completed = models.BooleanField(default=False)
    class Meta: 
        ordering = ["-created_at"]
    def __str__(self):
        return self.service_type + self.username
    