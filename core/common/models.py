from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class AbstractAuditableModel(models.Model):
    created_at = models.DateTimeField(_('date created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        abstract = True
