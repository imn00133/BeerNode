from django import forms
from django.forms.widgets import Input
from django.template.loader import render_to_string


class GetMapLocation(Input):

    def render(self, name, value, attrs=None, renderer=None):
        context = {
            'value': value,
            'name': name,
            'id': attrs['id']
        }

        html = render_to_string(
            'scrapapp/getmaplocation.html', context)

        # parent_html = super().render(name, value, attrs, renderer)

        return html
