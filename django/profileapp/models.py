from django.conf import settings
from django.db import models
from default_image.fields import DefaultStaticImageField


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    image = DefaultStaticImageField(upload_to='profile/', default_image_path='image/no_img.png', null=True, blank=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=200, null=True, blank=True)
