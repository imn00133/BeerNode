from django.urls import path
from django.views.generic import TemplateView

app_name = "scraplistapp"

urlpatterns = [
    path('list/', TemplateView.as_view(
        template_name= 'scraplistapp/list_oneline.html'), name='scraplist'),
]