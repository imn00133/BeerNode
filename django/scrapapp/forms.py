from django.forms import ModelForm
from django.forms import DateInput

from scrapapp.models import Scrap
from scrapapp.widgets import GetMapLocation


class ScrapCreationForm(ModelForm):
    class Meta:
        model = Scrap
        fields = ['beer_name', 'date', 'place', 'flavor', 'context', 'picture']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'place': GetMapLocation(attrs={'type': 'string'})
        }
