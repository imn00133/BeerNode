from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})