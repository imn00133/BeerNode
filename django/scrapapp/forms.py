from django.forms import ModelForm
from django.forms import DateInput

from scrapapp.models import Scrap
from .widgets import starWidget

class ScrapCreationForm(ModelForm):

    class Meta:
        model = Scrap

        fields = ['beer_name', 'date', 'place', 'lat', 'lng', 'flavor', 'context', 'picture', 'rating', 'sweet', 'sour', 'bitter', 'hoppy', 'fruity', 'malty']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'rating': starWidget,
            'sweet' : starWidget,
            'sour' : starWidget,
            'bitter' : starWidget,
            'hoppy' : starWidget,
            'fruity' : starWidget,
            'malty' : starWidget,
        }

