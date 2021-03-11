from django.forms import ModelForm
from django.forms import DateInput

from scrapapp.models import Scrap
from .widgets import starWidget, RangeInput


class ScrapCreationForm(ModelForm):

    class Meta:
        model = Scrap

        fields = ['beer_name', 'date', 'place', 'lat', 'lng', 'context', 'picture', 'rating', 'sweet', 'sour', 'bitter', 'hoppy', 'fruity', 'malty']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'rating': starWidget,
            'sweet': RangeInput,
            'sour': RangeInput,
            'bitter':RangeInput,
            'hoppy':RangeInput,
            'fruity':RangeInput,
            'malty':RangeInput
        }

