from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from beernode import settings
from scrapapp.views import ScrapCreateView, test, ScrapDetailView, ScrapUpdateView, ScrapDeleteView

app_name = "scrapapp"

urlpatterns = [
    path('', test, name='test'),
    path('create/', ScrapCreateView.as_view(), name='create'),
    path('update/<int:pk>', ScrapUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', ScrapDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', ScrapDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
