from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# Register your models here.
from core.budget.models import Budget, Transfer, BudgetGroup


class TransferAdmin(admin.TabularInline):
    list_display = ('transfer_type', 'amount', 'currency', 'created_at')
    model = Transfer


class BudgetAdminInline(admin.TabularInline):
    model = Budget.groups.through
    verbose_name = _("Budget")
    verbose_name_plural = _("Budgets")


class CollaboratorInlineAdmin(admin.TabularInline):
    model = BudgetGroup.collaborators.through
    verbose_name = _("Collaborator")
    verbose_name_plural = _("Collaborators")


class BudgetGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    model = BudgetGroup
    inlines = (BudgetAdminInline, CollaboratorInlineAdmin)


class BudgetGroupAdminInline(admin.TabularInline):
    model = BudgetGroup.budgets.through
    verbose_name = _("Group")
    verbose_name_plural = _("Groups")


class BudgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    model = Budget
    inlines = (TransferAdmin, BudgetGroupAdminInline)


admin.site.register(Budget, BudgetAdmin)
admin.site.register(BudgetGroup, BudgetGroupAdmin)
