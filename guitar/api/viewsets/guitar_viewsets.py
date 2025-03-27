from rest_framework import viewsets
from guitar.models import Guitar
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404
from guitar.api.serializers.guitar_serializer import GuitarSerializer
from rest_framework.response import Response

class GuitarViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Guitar instances.
    """
    queryset = Guitar.objects.all()
    serializer_class = GuitarSerializer

    # Optional: Add filtering, searching, or ordering if needed.
    # Example: 
    # def get_queryset(self):
    #     return Guitar.objects.filter(is_available=True)

    def retrieve(self, request, pk=None):
        try:
            product_guitar = get_object_or_404(Guitar,pk=pk)
            serializer = self.get_serializer(product_guitar)
            print(f"Retriview Method iS {serializer.data}") 
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Http404:
            return Response({'error1': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
       
