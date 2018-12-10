from django.db import models
from django.contrib.auth.models import User

class PassSite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField('Name of a site', max_length=120)
    site_url = models.CharField('Site\'s url', max_length=120)
    account_name = models.CharField('Name of your account',max_length=120)
    account_password = models.CharField('Password to your account', max_length=150)
