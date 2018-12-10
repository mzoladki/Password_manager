from django.urls import path
from .views import UserApiView, PassSiteApiView, PassSiteDetailApiView

urlpatterns = [
    path('users/', UserApiView.as_view(), name='users'),
    path('pass-site/', PassSiteApiView.as_view(), name='pass-site'),
    path('pass-site-detail/<int:pk>', PassSiteDetailApiView.as_view(), name='pass-site-detail')
]