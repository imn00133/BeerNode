from django_filters import FilterSet

from scrapapp.models import Scrap


class ScrapFilter(FilterSet):
    class Meta:
        model = Scrap
