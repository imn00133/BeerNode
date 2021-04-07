from django.conf import settings
from django.db import models

# Create your models here.
from scrapapp.models import Scrap


class Scraplist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scraplist', default='')
    scrap = models.ManyToManyField(Scrap)
    image = models.ImageField(upload_to='scraplist/', null=True)
    message = models.CharField(max_length=20, null=True)

    # filter_option =
