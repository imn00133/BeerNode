import django_filters

from scrapapp.models import Scrap


class ScrapFilter(django_filters.FilterSet):

    class Meta:
        model = Scrap
        fields = {
            'beer_name': ['icontains'],
            'place': ['icontains'],
            'rating': ['gte', 'lte'],
        }
