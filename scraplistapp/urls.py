from django.urls import path
from django.views.generic import TemplateView

app_name = "scraplistapp"

urlpatterns = [
    path('detail/', TemplateView.as_view(
        template_name= 'scraplistapp/list.html'), name='detail'),
    path('oneline/', TemplateView.as_view(
        template_name='scraplistapp/list_oneline.html'), name='oneline'),
    path('block/', TemplateView.as_view(
        template_name='scraplistapp/list_block.html'), name='block'),
]