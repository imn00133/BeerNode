from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from default_image.fields import DefaultStaticImageField


class Scrap(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자')
    beer_name = models.CharField(max_length=128, verbose_name='맥주 이름')
    date = models.DateField(null=True, verbose_name='마신 날짜')
    place = models.CharField(max_length=128, verbose_name='장소')
    lng = models.CharField(max_length=128, null=True, blank=True)
    lat = models.CharField(max_length=128, null=True, blank=True)
    context = models.TextField(verbose_name='내용')
    picture = DefaultStaticImageField(upload_to='scrap/', null=True, blank=True, default_image_path='image/no_img.png', verbose_name='사진')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일시')
    rating = models.FloatField(null=True, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='평점')
    sweet = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sour = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    bitter = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    hoppy = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fruity = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    malty = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
