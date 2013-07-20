from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

from easy_thumbnails.fields import ThumbnailerImageField


class User(AbstractUser):
    avatar = ThumbnailerImageField(upload_to='uploads/photos', blank=True)
    twitter = models.URLField(max_length=100)
    github = models.URLField(max_length=100)
    linkedin = models.URLField(max_length=100)

    def full_name(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
