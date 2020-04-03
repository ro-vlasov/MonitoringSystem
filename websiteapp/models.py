from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

class Device(models.Model):
    title = models.CharField(
        max_length=255,
    )
    serial_number = models.CharField(
        max_length=255,
    )
    quantity = models.CharField(
        max_length=255,
    )
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    dev_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4, 
        help_text="Unique ID for this particular Device"
    )
    border_value = models.FloatField(
        max_length=100
    )

    def get_absolute_url(self):
        return reverse('websiteapp:detail_device', args=[str(self.dev_id), 'alltime'])

    def get_title(self):
        return self.title
    
    def get_serial_number(self):
        return self.serial_number

    def get_quantity(self):
        return self.quantity
    
    def get_uuid(self):
        return self.dev_id

    def get_border_value(self):
        return self.border_value
        
    def __str__(self):
        return ' '.join([self.title, self.serial_number, self.quantity])

class Measurement(models.Model):
    time = models.DateTimeField(
        null=True,
    )
    value = models.FloatField(
        max_length=100
    )
    device_id = models.ForeignKey(
        Device, 
        on_delete=models.CASCADE,
        to_field='dev_id',
        default=uuid.uuid4,
    )
    ip_feedback = models.GenericIPAddressField(
        null=True
    )

    def __str__(self):
        return ' '.join([str(self.value), str(self.time)])






