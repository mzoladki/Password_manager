from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.views import View


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def pass_manager_view(request):
    return render(request, 'pass-manager.html')

def pass_manager_detail_view(request):
    return render(request, 'pass-manager-detail.html')