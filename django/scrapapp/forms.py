from django.forms import ModelForm
from django.forms import DateInput

from scrapapp.models import Scrap
from .widgets import starWidget

class ScrapCreationForm(ModelForm):
    class Meta:
        model = Scrap
        fields = ['beer_name', 'date', 'place', 'flavor', 'context', 'picture', 'rating']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'rating': starWidget,
        }
