from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserRegistration(models.Model):
    username = models.CharField(max_length=100)
    phonenumber = PhoneNumberField(max_length=255, default='phone number')
    location = models.CharField(max_length=255, default='Type here')
    # Add more fields as needed
