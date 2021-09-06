from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreateForm

class SignUpView(CreateView):
    form_class= CustomUserCreateForm
    template_name= 'account/signup.html'
    success_url= '/accounts/login' 

class LogoutConfirm(TemplateView):
    template_name= 'account/logoutconfirm.html'