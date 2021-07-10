from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from core.budget.dto import BudgetSerializer
from core.budget.models import Budget


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
