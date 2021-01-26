from django.urls import path

from scrapapp.views import test, ScrapCreateView

app_name = "scrapapp"

urlpatterns = [
    path('test/', test, name='test'),
    path('create/', ScrapCreateView.as_view(), name='create'),
]