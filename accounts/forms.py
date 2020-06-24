from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.forms import EmailInput, PasswordInput, TextInput


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "phone", "password1", "password2"]
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'Your Email'}),
            'username': TextInput(attrs={'placeholder': 'Your Username'}),
            'phone': TextInput(attrs={'placeholder': 'Your Phone'}),
            'password1': PasswordInput(attrs={'placeholder': 'Your Password'}),
            'password2': PasswordInput(attrs={'placeholder': 'Enter Re Password'}),
        }

