from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from feedapp.filters import ScrapFilter
from scrapapp.models import Scrap


class FeedView(ListView):
    model = Scrap
    context_object_name = 'scrap_list'
    template_name = 'feedapp/feed.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(writer_id=self.kwargs['pk'])
        qs = ScrapFilter(self.request.GET, queryset=qs)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['writer'] = User.objects.get(pk=self.kwargs['pk'])
        return context
