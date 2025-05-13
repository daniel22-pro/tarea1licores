from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, LicorViewSet, InventarioViewSet, VentaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'licores', LicorViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'ventas', VentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
