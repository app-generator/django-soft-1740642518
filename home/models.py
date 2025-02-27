# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    super admin = models.TextField(max_length=255, null=True, blank=True)
    admin = models.TextField(max_length=255, null=True, blank=True)
    user = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Toyota(models.Model):

    #__Toyota_FIELDS__
    top sales = models.TextField(max_length=255, null=True, blank=True)
    the most wanted car = models.CharField(max_length=255, null=True, blank=True)
    stuctur = models.TextField(max_length=255, null=True, blank=True)
    best employe of the month = models.TextField(max_length=255, null=True, blank=True)

    #__Toyota_FIELDS__END

    class Meta:
        verbose_name        = _("Toyota")
        verbose_name_plural = _("Toyota")



#__MODELS__END
