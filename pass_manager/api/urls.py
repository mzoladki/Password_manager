from django.urls import path
from .views import PassSiteApiView, PassSiteDetailApiView

urlpatterns = [
    path('pass-site/', PassSiteApiView.as_view(), name='pass-site'),
    path('pass-site-detail/', PassSiteDetailApiView.as_view(), name='pass-site-detail'),
]