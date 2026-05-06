# API
from rest_framework import viewsets

# MODELOS
from lecturas.models import Producto, Venta, DetalleVenta

# SERIALIZAERS
from .serializer import ProductooSerializer, DetalleVenta, VentaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductooSerializer
    queryset = Producto.objects.all().order_by('-id')


class DetalleVentaViewSet(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = DetalleVenta.objects.all().order_by('-id')

@api_view(['GET'])
def ultima_venta(request):
    venta = Venta.objects.order_by('-fecha_hora').first()

    if not venta:
        return Response({"mensaje": "No hay ventas registradas"}, status=404)

    serializer = VentaSerializer(venta)
    return Response(serializer.data)

@api_view(['POST'])
def crear_venta(request):
    data = request.data

    venta = Venta.objects.create()

    for item in data:
        producto = Producto.objects.get(id=item['producto_id'])

        if producto.stock < item['cantidad']:
            return Response({
                "error": f"Stock insuficiente para {producto.nombre}"
            }, status=400)

        DetalleVenta.objects.create(
            venta=venta,
            producto=producto,
            cantidad=item['cantidad']
           
        )

        # actualizar stock
        producto.stock -= item['cantidad']
        producto.save()

    return Response({
        "mensaje": "Venta realizada",
        "venta_id": venta.id
        
    })