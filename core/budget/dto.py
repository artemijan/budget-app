# Serializers define the API representation.
from rest_framework import serializers

from core.budget.models import Budget, BudgetGroup


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.StringRelatedField(many=True, allow_empty=True)

    class Meta:
        model = Budget
        fields = ('name', 'groups', 'owner')


class BudgetGroupSerializer(serializers.HyperlinkedModelSerializer):
    budgets = serializers.StringRelatedField(many=True, allow_empty=True)
    collaborators = serializers.StringRelatedField(many=True, allow_empty=True)

    class Meta:
        model = BudgetGroup
        fields = ('name', 'budgets', 'collaborators')
