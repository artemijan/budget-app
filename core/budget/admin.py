from django.contrib import admin

# Register your models here.
from core.budget.models import Budget, Transfer, BudgetGroup


class TransferAdmin(admin.TabularInline):
    list_display = ('transfer_type', 'amount', 'currency', 'created_at')
    model = Transfer


class BudgetAdminInline(admin.TabularInline):
    model = Budget.groups.through


class BudgetGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    model = BudgetGroup
    inlines = (BudgetAdminInline,)


class BudgetGroupAdminInline(admin.TabularInline):
    model = BudgetGroup.budgets.through


class BudgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    model = Budget
    inlines = (TransferAdmin, BudgetGroupAdminInline)


admin.site.register(Budget, BudgetAdmin)
admin.site.register(BudgetGroup, BudgetGroupAdmin)
