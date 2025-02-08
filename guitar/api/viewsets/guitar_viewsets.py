from rest_framework import viewsets
from guitar.models import Guitar
from guitar.api.serializers.guitar_serializer import GuitarSerializer

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
