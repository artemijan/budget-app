# Create your views here.
from rest_framework import viewsets
from core.budget.dto import BudgetSerializer, BudgetGroupSerializer, TransferSerializer, CollaboratorSerializer, \
    BudgetCreateSerializer
from core.budget.models import Budget, BudgetGroup, Transfer
from core.customer.models import User


class TransferViewSet(viewsets.ModelViewSet):
    serializer_class = TransferSerializer

    def get_queryset(self):
        return Transfer.objects.filter(budget_id=self.kwargs['budget_pk'])


class CollaboratorsViewSet(viewsets.ModelViewSet):
    serializer_class = CollaboratorSerializer

    def get_queryset(self):
        return User.objects.filter(budgetgroup_set__pk=self.kwargs['group_pk'])


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BudgetCreateSerializer
        return self.serializer_class


class BudgetGroupViewSet(viewsets.ModelViewSet):
    queryset = BudgetGroup.objects.all()
    serializer_class = BudgetGroupSerializer
