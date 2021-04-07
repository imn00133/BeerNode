from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, ListView

from scrapapp.models import Scrap
from listapp.models import Scraplist

from .filters import ScrapFilter

# global one


def oneline(request):
    scraps = Scrap.objects
    return render(request, 'listapp/list_oneline.html', {'scraps':scraps})


# class ScraplistDetailView(DetailView):
#     model = Scraplist
#     context_object_name = 'target_scraplist'
#     template_name = 'listapp/list.html'


class ScraplistListView(ListView):
    model = Scrap
    context_object_name = 'scrap_list'
    template_name = 'listapp/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Scrap.objects.filter(writer_id=self.kwargs['pk'])
        context['filter'] = ScrapFilter(self.request.GET, queryset=context['object_list'])
        return context
