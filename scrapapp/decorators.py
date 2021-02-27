from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from scrapapp.models import Scrap


def scrap_ownership_required(func):
    def decorated(request, *args, **kwargs):
        scrap = Scrap.objects.get(pk=kwargs['pk'])
        if not scrap.writer == request.user:
            return HttpResponseForbidden()
        else:
            return func(request, *args, **kwargs)

    return decorated
