from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import PassSite

class PassManagerAddView(FormView):
    pass

class PassManagerUpdateView(FormView):
    pass
    
class PassManagerView(ListView):
    model = PassSite
    template_name = 'pass-manager.html'
    context_object_name = 'content'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        print(queryset)
        return queryset


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PassManagerDetailView(DetailView):
    model = PassSite
    template_name = 'pass-manager-detail.html'
    context_object_name = 'content'
