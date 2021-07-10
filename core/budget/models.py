# Create your models here.
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from core.common.enums import ChoiceEnum, Currency
from core.common.models import AbstractAuditableModel


class Budget(AbstractAuditableModel):
    name = models.CharField(_("Budget name"), max_length=255)
    groups = models.ManyToManyField('budget.BudgetGroup', through='budget.BudgetToGroupRelation')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("An owner of the budget"),
                              on_delete=models.CASCADE)

    def __str__(self):
        return f"Budget: {self.name}"

    @cached_property
    def incomes(self):
        return self.transfers.filter(Transfer.TransferTypes.INCOME.name)

    @cached_property
    def outcomes(self):
        return self.transfers.filter(Transfer.TransferTypes.OUTCOME.name)


class BudgetToGroupRelation(AbstractAuditableModel):
    group = models.ForeignKey('budget.BudgetGroup', on_delete=models.CASCADE)
    budget = models.ForeignKey('budget.Budget', on_delete=models.CASCADE)


class BudgetGroup(AbstractAuditableModel):
    name = models.CharField(_("Group name"), max_length=255)
    budgets = models.ManyToManyField('budget.Budget', through='budget.BudgetToGroupRelation')

    def __str__(self):
        return f"Budget group {self.name}"


class Transfer(AbstractAuditableModel):
    class TransferTypes(ChoiceEnum):
        INCOME = "Income"
        OUTCOME = "Outcome"

    PRECISION = 100
    budget = models.ForeignKey('budget.Budget', related_name='transfers', on_delete=models.CASCADE)
    transfer_type = models.CharField(_("Transfer type"), choices=TransferTypes.choices(), max_length=255)
    monetary_units = models.PositiveIntegerField(_("Monetary units (e.g. 10$==1000 monetary units, cents)"))
    currency = models.CharField(_("Currency iso alpha 3"), max_length=3, choices=Currency.choices())
    description = models.CharField(_("Description of the transfer"), max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.transfer_type} transfer of {self.currency.upper()}{self.amount}"

    @property
    def amount(self):
        return self.monetary_units / self.PRECISION
