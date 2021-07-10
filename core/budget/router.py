from rest_framework import routers

from core.budget.views import BudgetViewSet

router = routers.DefaultRouter()

router.register(r'budgets', BudgetViewSet)
