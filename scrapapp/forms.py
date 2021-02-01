from django.forms import ModelForm
from django import forms

from scrapapp.models import Scrap


class ScrapCreationForm(ModelForm):
    class Meta:
        model = Scrap
        fields = ['beer_name', 'place', 'flavor', 'context', 'picture']
        # date = forms.DateTimeField(
        #     input_formats=['%d/%m/%Y'],
        #     widget = forms.DateTimeInput(attrs={
        #     'class': 'form-control datetimepicker-input',
        #     'data-target': '#datetimepicker1'
        # })
        # )