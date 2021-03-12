from django.urls import path
from django.views.generic import TemplateView

from scrapapp.views import ScrapCreateView, test, ScrapDetailView, ScrapUpdateView, ScrapDeleteView

app_name = "scrapapp"

urlpatterns = [
    path('', test, name='test'),
    path('create/', ScrapCreateView.as_view(), name='create'),
    path('update/<int:pk>', ScrapUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', ScrapDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', ScrapDeleteView.as_view(), name='delete'),
]
