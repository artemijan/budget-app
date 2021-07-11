from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet

from core.customer.models import User


class CustomerService:
    def get_user(self, pk: int, **kwargs) -> User:
        return User.objects.get(pk=pk, **kwargs)

    def get_user_or_none(self, pk: int, **kwargs) -> Optional[User]:
        try:
            return self.get_user(pk, **kwargs)
        except ObjectDoesNotExist:
            pass

    def get_users_by_id(self, ids: list) -> QuerySet:
        return User.objects.filter(pk__in=ids)
