from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.forms import EmailInput, PasswordInput


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["email","password1", "password2"]
        widgets = {
            'email': EmailInput(attrs={'class': 'frm-group', 'placeholder':'Your Email'}),
            'password1': PasswordInput(attrs={'class': 'frm-group', 'placeholder':'Your Password'}),
            'password2': PasswordInput(attrs={'class': 'frm-group', 'placeholder':'Enter Re Password'}),
        }
