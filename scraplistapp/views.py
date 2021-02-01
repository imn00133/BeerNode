from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView

from scraplistapp.models import Scraplist


class ScraplistDetailView(DetailView):
    model = Scraplist
    context_object_name = "scraplist"
    template_name = 'scraplistapp/list.html'
