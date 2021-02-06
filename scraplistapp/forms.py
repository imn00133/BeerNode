from django.forms import ModelForm

from scraplistapp.models import Scraplist


class ScraplistCreationForm(ModelForm):
    class Meta:
        model = Scraplist
        fields = ['image', 'message']


