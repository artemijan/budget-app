from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .customer.router import router as customer_router
from .budget.router import budgets_router as budgets_sub_router
from .budget.router import group_router as group_sub_router
from .budget.router import router as budget_router

router = routers.DefaultRouter()
router.registry.extend(budget_router.registry)
router.registry.extend(customer_router.registry)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(budgets_sub_router.urls)),
    url(r'^', include(group_sub_router.urls)),
]
