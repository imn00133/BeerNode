from django.urls import path

from beerapp.views import BeerDetailView

app_name = "beerapp"

urlpatterns = [
    path('detail/<int:pk>', BeerDetailView.as_view(), name='detail'),
]
