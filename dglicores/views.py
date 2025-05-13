from rest_framework import viewsets
from .models import Cliente, Licor, Inventario, Venta
from .serializer import ClienteSerializer, LicorSerializer, InventarioSerializer, VentaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class LicorViewSet(viewsets.ModelViewSet):
    queryset = Licor.objects.all()
    serializer_class = LicorSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
