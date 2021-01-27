<<<<<<< HEAD
from django.db import models

# Create your models here.
=======
from django.conf import settings
from django.db import models

# Create your models here.

class Scrap(models.Model):
    # writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    beer_name = models.CharField(max_length=128, verbose_name='맥주 이름')
    # date = models.DateField()
    place = models.CharField(max_length=128, verbose_name='장소')
    flavor = models.CharField(max_length=128, verbose_name='맛')
    context = models.TextField(verbose_name='내용')
    picture = models.ImageField(upload_to='scrap/', null=True, verbose_name='사진')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일시')
>>>>>>> origin/main
