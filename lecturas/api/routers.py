from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'producto', views.ProductoViewSet, 'producto')
router.register(r'detalle_venta', views.DetalleVentaViewSet, 'detalle_venta')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/crear_venta/', views.crear_venta, name='crear_venta'),
    path('api/ultima_venta/', views.ultima_venta, name='ultima_venta'),
    path('api/marcar_ultima_venta_servida/', views.marcar_ultima_venta_servida, name='marcar_ultima_venta_servida')
    
   
]