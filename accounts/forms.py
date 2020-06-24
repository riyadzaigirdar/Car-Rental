from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.forms import EmailInput, PasswordInput, TextInput, ModelForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "phone", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Phone'})
        self.fields['password1'].widget=PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget=PasswordInput(attrs={'placeholder': 'Repeat Password'})
