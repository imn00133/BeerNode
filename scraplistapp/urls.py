from django.urls import path
from django.views.generic import TemplateView

from scraplistapp.views import oneline

app_name = "scraplistapp"

urlpatterns = [
    path('detail/', TemplateView.as_view(
        template_name= 'scraplistapp/list.html'), name='detail'),
    path('oneline/', oneline, name='oneline'),
    path('block/', TemplateView.as_view(
        template_name='scraplistapp/list_block.html'), name='block'),
    path('home/', TemplateView.as_view(
        template_name='scraplistapp/test_home.html'), name='test_home'),
]