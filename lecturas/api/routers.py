from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'producto', views.ProductoServidoViewSet, 'producto')



urlpatterns = [
    path('api/', include(router.urls)),
    path('api/recibir_datos/', views.recibir_lectura_esp8266, name='recibir_datos')
   
]