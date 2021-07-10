# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.common.models import AbstractAuditableModel


class Budget(AbstractAuditableModel):
    pass


class AbstractTransfer(AbstractAuditableModel):
    monetary_units = models.PositiveIntegerField(_("Monetary units (e.g. 10$==1000 monetary units, cents)"))
    currency = models.CharField(_("Currency iso alpha 3"), max_length=3)

    class Meta:
        abstract = True


class Income(AbstractTransfer):
    pass


class Expense(AbstractTransfer):
    pass
