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
        context['rating'] = scrap_list.aggregate(Avg('rating')).get('rating__avg')

        flavor_list = ['sweet', 'sour', 'bitter', 'hoppy', 'fruity', 'malty']
        flavor_dic = {}
        for flavor in flavor_list:
            flavor_dic[flavor] = scrap_list.aggregate(Avg(flavor)).get(flavor + '__avg')
        context['flavor_dic'] = flavor_dic

        return context
