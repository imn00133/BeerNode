from django.urls import path

from feedapp.views import FeedView

app_name = "feedapp"

urlpatterns = [
    path('<int:pk>', FeedView.as_view(), name='feed'),
]
