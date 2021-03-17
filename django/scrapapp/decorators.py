from django.shortcuts import render

from scrapapp.models import Scrap


def scrap_ownership_required(func):
    def decorated(request, *args, **kwargs):
        scrap = Scrap.objects.get(pk=kwargs['pk'])
        if not scrap.writer == request.user:
            return render(request, template_name='403.html')
        else:
            return func(request, *args, **kwargs)
    return decorated
