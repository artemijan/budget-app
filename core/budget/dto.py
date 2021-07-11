# Serializers define the API representation.
from django.conf import settings
from rest_framework import serializers

from core.budget.models import Budget, BudgetGroup


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.StringRelatedField(many=True, allow_empty=True)

    class Meta:
        model = Budget
        fields = ('url', 'name', 'groups', 'owner')


class BudgetGroupSerializer(serializers.HyperlinkedModelSerializer):
    budgets = serializers.StringRelatedField(many=True, allow_empty=True)
    collaborators = serializers.StringRelatedField(many=True, allow_empty=True)

    class Meta:
        model = BudgetGroup
        fields = ('url', 'name', 'budgets', 'collaborators')


class CollaboratorSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=0)
