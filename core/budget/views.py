from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from core.budget.dto import BudgetSerializer, BudgetGroupSerializer
from core.budget.models import Budget, BudgetGroup


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetGroupViewSet(viewsets.ModelViewSet):
    queryset = BudgetGroup.objects.all()
    serializer_class = BudgetGroupSerializer
