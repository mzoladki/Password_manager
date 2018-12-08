from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import PassManagerView, SignUpView, PassManagerDetailView, PassManagerAddView

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html',redirect_field_name='/pass-manager/', redirect_authenticated_user=True), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('pass-manager/', PassManagerView.as_view(), name='pass-manager'),
    path('pass-manager/<int:pk>', PassManagerDetailView.as_view(), name='pass-manager-details'),
    path('add-pass-manager/', PassManagerAddView.as_view(), name='pass-manager-add')
]