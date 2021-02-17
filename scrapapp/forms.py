from django.forms import ModelForm

from scrapapp.models import Scrap


class ScrapCreationForm(ModelForm):
    class Meta:
        model = Scrap
        fields = ['beer_name', 'date', 'place', 'flavor', 'context', 'picture']
