from django.db import models
from django.contrib.auth.models import User

class PassSite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField('Name of a site', max_length=120)
    site_url = models.CharField('Site\'s url', max_length=120)
    account_name = models.CharField('Name of your account',max_length=120)
    account_password = models.CharField('Password to your account', max_length=150)

    def __str__(self):
        return "{}, site_name: {}, site_url: {}, account_name: {}, account_password: {}".format(self.user, self.site_name, self.site_url, self.account_name, self.account_password)
