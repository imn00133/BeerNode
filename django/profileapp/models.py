from django.conf import settings
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    username = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=200, null=True, blank=True)