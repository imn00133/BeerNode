from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from profileapp.models import Profile

has_ownership = [account_ownership_required, login_required]


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accountapp/create.html'

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('profileapp:create'))


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'
    success_url = reverse_lazy('test_home')


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('test_home')
    template_name = 'accountapp/delete.html'


class AccountLoginView(LoginView):
    def form_valid(self, form):
        login(self.request, form.get_user())
        self.form = form
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        username = self.form.cleaned_data['username']
        target_user = User.objects.get(username=username)
        try:
            target_profile = Profile.objects.get(user=target_user)
            return reverse_lazy('test_home')
        except Profile.DoesNotExist:
            return reverse_lazy('profileapp:create')
