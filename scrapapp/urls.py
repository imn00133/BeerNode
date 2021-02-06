from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from beernode import settings
from scrapapp.views import ScrapCreateView, test, ScrapDetailView

app_name = "scrapapp"

urlpatterns = [
    path('', test, name='test'),
    path('create/', ScrapCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ScrapDetailView.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
