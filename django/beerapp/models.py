from django.db import models


class Beer(models.Model):
    beer_name = models.CharField(max_length=128, verbose_name='맥주 이름')