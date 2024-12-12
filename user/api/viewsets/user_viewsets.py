from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.api.serializers.user_serializers import UserSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = None

    ''' def get_object(self,pk):
        return get_object_or_404(User,pk=pk)'''
    
    def get_queryset(self):
        
        return self.get_serializer().Meta.model.objects.all()
    '''def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active = True)
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()'''
    
    def list(self,request):
        user_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(user_serializer.data,status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        """
        GET /users/{id}/ - Retrieve a specific user.
        """
        instance = self.get_object()
        serializer= self.get_serializer(instance)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        """
        POST /users/ - Create a new user.
        """
        serializer = self.get_serializer(data=request.data)
    
        if serializer.is_valid(raise_exception = True):
           user = serializer.save()
           '''response_data ={
               'id':user.id,
               'username': user.username,
               'email': user.email

           }'''

        response_data = serializer.data.copy()
        response_data.pop('password',None)
    
        return Response(response_data,status= status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        partial = False  # For full update
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        # Remove password fields from the response
        response_data = serializer.data.copy()
        response_data.pop('password', None)
       # response_data.pop('password_confirm', None)
        return Response(response_data)
    
    def partial_update(self, request, *args, **kwargs):
        """
        PATCH /users/{id}/ - Update a user's details partially.
        """
        partial = True  # For partial update
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        # Remove password fields from the response
        response_data = serializer.data.copy()
        response_data.pop('password', None)
       # response_data.pop('password_confirm', None)
        return Response(response_data)
    
    def destroy(self, request, *args, **kwargs):
        """
        DELETE /users/{id}/ - Delete a user.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

