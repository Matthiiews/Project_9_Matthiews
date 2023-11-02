from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignupForm(UserCreationForm):
    """form to register"""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1", "password2")


class LoginForm(forms.Form):
    """login form to user interphase"""

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class AboForm(forms.Form):
    """form for the abonnement page, to follow and unfollow users"""

    search = forms.CharField(max_length=50, label=False)

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_search(self):
        search = self.cleaned_data["search"]

        # impossible to follow yourself:
        if self.user and self.user.username == search:
            # replaced with messages in view
            raise forms.ValidationError("You can not follow yourself!")

        # impossible to follow an admin/superuser:
        if User.objects.filter(username=search, is_superuser=True).exists():
            # replaced with messages in view
            raise forms.ValidationError(
                "Please choose an other name to follow!")

        return search


class FollowUserButton(forms.Form):
    searched_to_follow = forms.CharField(widget=forms.HiddenInput())


class SearchUser(forms.Form):
    search = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Rechercher un utilisateur'
            }
        )
    )
    search_user_id = forms.BooleanField(widget=forms.HiddenInput, initial=True)
