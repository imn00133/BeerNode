from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from profileapp.forms import ProfileCreationForm


class AccountCreationForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'profile': ProfileCreationForm,
    }


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True
