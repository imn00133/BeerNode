from django.urls import path
from django.views.generic import TemplateView

app_name = "scraplistapp"

urlpatterns = [
    path('scraplist/', TemplateView.as_view(template_name= 'scraplistapp/list.html'), name='scraplist'),
]