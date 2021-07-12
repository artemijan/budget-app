from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework import routers
from core.budget.views import BudgetViewSet, BudgetGroupViewSet, TransferViewSet, CollaboratorsViewSet

router = routers.DefaultRouter()
router.register(r'budgets', BudgetViewSet)
budgets_router = NestedSimpleRouter(router, r'budgets', lookup='budget')
budgets_router.register(
    r'transfers', TransferViewSet, basename='transfer'
)
router.register(r'budget-groups', BudgetGroupViewSet)
group_router = NestedSimpleRouter(router, r'budget-groups', lookup='group')
group_router.register(r'collaborators', CollaboratorsViewSet, basename='collaborator')
