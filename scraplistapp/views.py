from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView

from scrapapp.models import Scrap
from scraplistapp.models import Scraplist

def oneline(request):
    scraps = Scrap.objects
    return render(request, 'scraplistapp/list_oneline.html', {'scraps':scraps})

class ScraplistDetailView(DetailView):
    model = Scraplist
    scraps = Scrap.objects
    context_object_name = "scraplist"
    template_name = 'scraplistapp/list.html'
