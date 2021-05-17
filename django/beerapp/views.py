from django.views.generic import DetailView

from beerapp.models import Beer


class BeerDetailView(DetailView):
    model = Beer
    context_object_name = 'target_beer'
    template_name = 'beerapp/detail.html'