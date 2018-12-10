from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.views import View
import jwt


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

def pass_manager_share_view(request):
    token = request.GET.get('token', '')
    print('token: ')
    print(token)
    print(token[2:])
    encoded_token = jwt.decode(token, 'secret', algorithms=['HS256'])
    print(encoded_token)

    return render(request, 'pass-manager-share.html')