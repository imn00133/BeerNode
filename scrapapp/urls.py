from django.urls import path

<<<<<<< HEAD
app_name = "scrapapp"

urlpatterns = [
    path('scrap/', ),
=======
from scrapapp.views import test, ScrapCreateView

app_name = "scrapapp"

urlpatterns = [
    path('test/', test, name='test'),
    path('create/', ScrapCreateView.as_view(), name='create'),
>>>>>>> origin/main
]