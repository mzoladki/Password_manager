from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, pass_manager_view, pass_manager_detail_view


urlpatterns = [
    path('', LoginView.as_view(template_name='login.html', redirect_field_name='/pass-manager/', redirect_authenticated_user=True), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('pass-manager/', pass_manager_view, name='pass-manager'),
    path('pass-manager-details/', pass_manager_detail_view, name='pass-manager-details')
]