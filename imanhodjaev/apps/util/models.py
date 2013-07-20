from django.db import models


class AbstractDatetime(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
