from rest_framework import viewsets
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer
from .permissions import IsManager, IsCustomer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username' 

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsManager]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsCustomer]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'authentication_token': response.data['authentication_token']})
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_superuser and instance.username != request.user.username:
            return Response({'detail': 'Only the superuser can update their own account.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_superuser and instance.username != request.user.username:
            return Response({'detail': 'Only the superuser can partially update their own account.'}, status=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_superuser:
            return Response({'detail': 'Superuser cannot be deleted.'}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({'detail': 'User successfully deleted.'}, status=status.HTTP_200_OK)