from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.customer.dto import UserSerializer, PasswordSerializer
from core.customer.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'], name='Create a password', serializer_class=PasswordSerializer)
    def passwords(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
