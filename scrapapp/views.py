from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from scrapapp.forms import ScrapCreationForm
from scrapapp.models import Scrap


def test(request):
    scraps = Scrap.objects
    return render(request, 'scrapapp/test.html', {'scraps':scraps})


class ScrapCreateView(CreateView):
    model = Scrap
    form_class = ScrapCreationForm
    success_url = reverse_lazy('scraplistapp:oneline')
    template_name = 'scrapapp/create.html'



class ScrapDetailView(DetailView):
    model = Scrap
    context_object_name = 'target_beer'
    template_name = 'scrapapp/detail.html'
