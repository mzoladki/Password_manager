from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.views import View
import jwt
from django.contrib.messages import constants as messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings


class SignUpView(SuccessMessageMixin, FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = '/'
    success_message = 'Account created successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@login_required(login_url=settings.LOGOUT_REDIRECT_URL)
def pass_manager_view(request):
    return render(request, 'pass-manager.html')
