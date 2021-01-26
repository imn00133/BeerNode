from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from scrapapp.forms import ScrapCreationForm
from scrapapp.models import Scrap


def test(request):
    return HttpResponse('test message')

class ScrapCreateView(CreateView):
    model = Scrap
    form_class = ScrapCreationForm
    success_url = reverse_lazy('scrapapp:test')
    template_name = 'scrapapp/create.html'