from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from accounts.forms import SignUpForm
from django.urls import reverse_lazy
from accounts.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

import re
# Create your views here.

class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form.save()
        return super(SignUp, self).form_valid(form)


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        next = self.request.POST['next']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            if next is not None:
                next = re.sub(r'\s+', '', next)
                next = next[22:]
                super(LoginView, self).form_valid(form)
                return redirect(next)
        return super(LoginView, self).form_valid(form)


class LogoutView(LoginRequiredMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'app_login/login.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')


