from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from feedapp.filters import ScrapFilter
from scrapapp.models import Scrap


class ScrapListView(ListView):
    model = Scrap
    context_object_name = 'scrap_list'
    template_name = 'listapp/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Scrap.objects.filter(writer_id=self.kwargs['pk'])
        context['filter'] = ScrapFilter(self.request.GET, queryset=context['object_list'])
        return context
