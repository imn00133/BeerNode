from django.forms import ModelForm
from django.forms import DateInput

from scrapapp.models import Scrap


class ScrapCreationForm(ModelForm):

    class Meta:
        model = Scrap
        fields = ['beer_name', 'date', 'place', 'lat', 'lng', 'flavor', 'context', 'picture']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }

