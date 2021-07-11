# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import BindingDict

from core.budget.dto import BudgetSerializer, BudgetGroupSerializer, CollaboratorSerializer
from core.budget.models import Budget, BudgetGroup
from core.customer.service import CustomerService


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetGroupViewSet(viewsets.ModelViewSet):
    queryset = BudgetGroup.objects.all()
    serializer_class = BudgetGroupSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer_service = CustomerService()

    @action(detail=True, methods=['post'], name='Add a collaborator', serializer_class=CollaboratorSerializer)
    def collaborators(self, request, pk=None):
        if isinstance(request.data, list):
            return self.handle_collaborator_bulk(CollaboratorSerializer(data=request.data, many=True))
        else:
            return self.handle_single_collaborator(CollaboratorSerializer(data=request.data), pk=pk)

    def handle_single_collaborator(self, serializer, pk=None):
        group = self.get_object()
        if serializer.is_valid():
            user = self.customer_service.get_user_or_none(serializer.validated_data['pk'])
            if user:
                group.collaborators.add(user)
                return Response({})
        # todo implement generic logic for bad request error codes
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def handle_collaborator_bulk(self, serializer, pk=None):
        group = self.get_object()
        if serializer.is_valid():
            ids = [item['id'] for item in serializer.validated_data]
            users = list(self.customer_service.get_users_by_id(ids))
            if len(users) == len(ids):
                group.collaborators.add(*users)
                return Response({})
        # todo implement generic logic for bad request error codes
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
