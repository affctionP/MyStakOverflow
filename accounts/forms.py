from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import USER


class UserCreateForm(UserCreationForm):
    class meta:
        model = USER
        fields = ('email',)


class UserChangeForm(UserChangeForm):
    class meta:
        model = USER
        fields = ('email',)

