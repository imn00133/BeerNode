from django.urls import path

from scrapapp.views import test

app_name = "scrapapp"

urlpatterns = [
    path('test/', test, name='test')
]