from django.db import models

# Create your models here.
from scrapapp.models import Scrap


class Scraplist(models.Model):
    #user = models.OneToOneField(User, 머시기머시기
    #나중에 User DB 만들어지면 해당 유저와 1:1 대응 필요
    scrap = Scrap

    # filter_option =
