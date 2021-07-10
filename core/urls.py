from rest_framework import routers

from .customer.router import router as customer_router
from .budget.router import router as budget_router

router = routers.DefaultRouter()
router.registry.extend(budget_router.registry)
router.registry.extend(customer_router.registry)
urlpatterns = router.urls
