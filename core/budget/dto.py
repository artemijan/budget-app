# Serializers define the API representation.
from rest_framework import serializers
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer, NestedHyperlinkedRelatedField

from core.budget.models import Budget, BudgetGroup, Transfer, BudgetGroupToUserRelation
from core.customer.models import User


class TransferSerializer(NestedHyperlinkedModelSerializer):
    amount = serializers.DecimalField(12, 2)
    parent_lookup_kwargs = {
        'budget_pk': 'budget_id',
    }

    class Meta:
        model = Transfer
        fields = ('url', 'transfer_type', 'amount', 'currency', 'description')


class CollaboratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'email')


class BudgetSerializer(NestedHyperlinkedModelSerializer):
    groups = serializers.StringRelatedField(many=True, allow_empty=True)
    transfers = TransferSerializer(many=True)

    class Meta:
        model = Budget
        fields = ('url', 'name', 'groups', 'owner', 'transfers')


class BudgetGroupSerializer(NestedHyperlinkedModelSerializer):
    budgets = serializers.StringRelatedField(many=True, allow_empty=True)
    collaborators = CollaboratorSerializer(many=True)

    class Meta:
        model = BudgetGroup
        fields = ('url', 'name', 'budgets', 'collaborators')
