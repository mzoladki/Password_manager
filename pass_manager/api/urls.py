from django.urls import path
from .views import PassSiteApiView, PassSiteDetailApiView, CreatePassSiteShareApiView

urlpatterns = [
    path('pass-site/', PassSiteApiView.as_view(), name='pass-site'),
    path('pass-site-detail/', PassSiteDetailApiView.as_view(), name='pass-site-detail'),
    path('create-pass-site-share/', CreatePassSiteShareApiView.as_view(), name= 'create-pass-site-share')

]