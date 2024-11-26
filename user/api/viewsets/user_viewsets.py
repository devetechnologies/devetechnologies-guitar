from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from user.models import User
from user.api.serializers.user_serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = None

    def get_object(self,pk):
        return get_object_or_404(User,pk=pk)
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()
    
    def list(self,request):
        user_serializer = self.get_serializer(self.get_queryset(),many=True)

        return Response(user_serializer.data,status=status.HTTP_200_OK)

