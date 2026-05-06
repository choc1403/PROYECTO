# SERIALIZADOR
from rest_framework import serializers


# MODELOS
from lecturas.models import Producto, DetalleVenta, Venta






class ProductooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'




class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre']


class DetalleVentaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad']

   


class VentaSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True)
  

    class Meta:
        model = Venta
        fields = ['id', 'fecha_hora', 'detalles']

   
 