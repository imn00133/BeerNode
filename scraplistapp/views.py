from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, ListView

from scrapapp.models import Scrap
from scraplistapp.models import Scraplist

def oneline(request):
    scraps = Scrap.objects
    return render(request, 'scraplistapp/list_oneline.html', {'scraps':scraps})

class ScraplistDetailView(DetailView):
    model = Scraplist
    context_object_name = 'target_scraplist'
    template_name = 'scraplistapp/list.html'

    def get_context_data(self, **kwargs):
        object_list = Scrap.objects.filter(project=self.get_object())
        return super(ScraplistDetailView, self).get_context_data(
            object_list=object_list, **kwargs)
