from django.db.models import Avg
from django.views.generic import DetailView

from beerapp.models import Beer
from scrapapp.models import Scrap


class BeerDetailView(DetailView):
    model = Beer
    context_object_name = 'target_beer'
    template_name = 'beerapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scrap_list = Scrap.objects.filter(beer_name=self.get_object().beer_name)
        rating = scrap_list.aggregate(Avg('rating'))
        print(scrap_list)
        print(rating)
        return context
