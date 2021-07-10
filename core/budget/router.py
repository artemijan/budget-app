from rest_framework import routers

from core.budget.views import BudgetViewSet, BudgetGroupViewSet

router = routers.DefaultRouter()

router.register(r'budgets', BudgetViewSet)
router.register(r'budget-groups', BudgetGroupViewSet)
