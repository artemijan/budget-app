# Serializers define the API representation.
from rest_framework import serializers

from core.budget.models import Budget


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = Budget
        fields = ('name', 'groups', 'owner')
