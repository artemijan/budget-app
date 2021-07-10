from rest_framework import routers

from core.customer.views import UserViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
