from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from feedapp.filters import ScrapFilter
from scrapapp.models import Scrap


class ScrapListView(ListView):
    model = Scrap
    context_object_name = 'scrap_list'
    template_name = 'listapp/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(writer_id=self.kwargs['pk'])
        qs = ScrapFilter(self.request.GET, queryset=qs)
        return qs
