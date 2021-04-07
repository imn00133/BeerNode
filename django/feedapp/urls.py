from django.urls import path

from feedapp.views import ScrapListView

app_name = "feedapp"

urlpatterns = [
    path('feed/<int:pk>', ScrapListView.as_view(), name='feed'),
]
