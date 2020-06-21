from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class SignUp(TemplateView):
    template_name = "accounts/signup.html"
