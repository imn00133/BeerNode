from django.forms import ModelForm

from listapp.models import Scraplist


class ScraplistCreationForm(ModelForm):
    class Meta:
        model = Scraplist
        fields = ['image', 'scrap', 'message']
