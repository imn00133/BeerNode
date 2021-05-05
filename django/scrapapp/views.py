from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from scrapapp.decorators import scrap_ownership_required
from scrapapp.forms import ScrapCreationForm
from scrapapp.models import Scrap

HAS_OWNERSHIP = [scrap_ownership_required, login_required]


def test(request):
    scraps = Scrap.objects
    return render(request, 'scrapapp/test.html', {'scraps': scraps})


class ScrapCreateView(CreateView):
    model = Scrap
    form_class = ScrapCreationForm
    template_name = 'scrapapp/create_form.html'

    def form_valid(self, form):
        temp = form.save(commit=False)
        temp.writer = self.request.user
        return super().form_valid(form)


class ScrapDetailView(DetailView):
    model = Scrap
    context_object_name = 'target_beer'
    template_name = 'scrapapp/detail_table.html'


@method_decorator(HAS_OWNERSHIP, 'get')
@method_decorator(HAS_OWNERSHIP, 'post')
class ScrapUpdateView(UpdateView):
    model = Scrap
    context_object_name = 'target_beer'
    form_class = ScrapCreationForm
    template_name = 'scrapapp/update.html'


@method_decorator(HAS_OWNERSHIP, 'get')
@method_decorator(HAS_OWNERSHIP, 'post')
class ScrapDeleteView(DeleteView):
    model = Scrap
    context_object_name = 'target_beer'
    template_name = 'scrapapp/delete.html'

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse_lazy('scraplistapp:list', kwargs={'pk': user_id})
