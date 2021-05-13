from django.db import models

from default_image.fields import DefaultStaticImageField


class Beer(models.Model):
    beer_name = models.CharField(max_length=128, verbose_name='맥주 이름')
    rating = models.FloatField(null=True, blank=True)
    num_scraps = models.IntegerField(default=0)
    sweet = models.FloatField(null=True, blank=True)
    malty = models.FloatField(null=True, blank=True)
    hoppy = models.FloatField(null=True, blank=True)
    sour = models.FloatField(null=True, blank=True)
    bitter = models.FloatField(null=True, blank=True)
    fruity = models.FloatField(null=True, blank=True)
    place1 = models.CharField(max_length=128, blank=True)
    place2 = models.CharField(max_length=128, blank=True)
    image = DefaultStaticImageField(upload_to='beer/', default_image_path='image/no_img.png', null=True, blank=True)
    body = models.TextField(blank=True)
    brewery = models.CharField(max_length=128, blank=True)
    date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=128, blank=True)
    genre = models.CharField(max_length=128, blank=True)
    abv = models.FloatField(null=True, blank=True)
