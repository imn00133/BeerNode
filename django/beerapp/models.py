from django.db import models

from default_image.fields import DefaultStaticImageField


class Beer(models.Model):
    beer_name = models.CharField(max_length=128, verbose_name='맥주 이름')
    image = DefaultStaticImageField(upload_to='beer/', default_image_path='image/no_img.png', null=True, blank=True)
    body = models.TextField(blank=True)
    brewery = models.CharField(max_length=128, blank=True)
    date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=128, blank=True)
    genre = models.CharField(max_length=128, blank=True)
    abv = models.FloatField(null=True, blank=True)
