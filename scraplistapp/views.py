from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, ListView

from scrapapp.models import Scrap
from scraplistapp.models import Scraplist

global one

def oneline(request):
    scraps = Scrap.objects
    return render(request, 'scraplistapp/list_oneline.html', {'scraps':scraps})

class ScraplistDetailView(DetailView):
    model = Scraplist
    context_object_name = 'target_scraplist'
    template_name = 'scraplistapp/list.html'

class ScraplistListView(ListView):
    model = Scrap
    context_object_name = 'scrap_list'
    template_name = 'scraplistapp/list.html'