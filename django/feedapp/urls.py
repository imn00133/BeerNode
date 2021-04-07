from django.urls import path
from django.views.generic import TemplateView

from listapp.views import oneline, ScraplistListView

app_name = "feedapp"

urlpatterns = [
    path('feed/<int:pk>', ScraplistListView.as_view(), name='list'),
]