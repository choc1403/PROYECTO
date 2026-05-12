# API
from rest_framework import viewsets
from rest_framework import status

# MODELOS
from lecturas.models import ProductoServido, Venta, DetalleVenta

# SERIALIZAERS
from .serializer import ProductoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductoServidoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = ProductoServido.objects.all().order_by('-id')

"""
class DetalleVentaViewSet(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = DetalleVenta.objects.all().order_by('-id')

@api_view(['GET'])
def ultima_venta(request):
    venta = Venta.objects.order_by('-fecha_hora').exclude(servido = True).first()

    if not venta:
        return Response({"mensaje": "No hay ventas registradas"}, status=404)

    serializer = VentaSerializer(venta)
    return Response(serializer.data)

@api_view(['POST'])
def marcar_ultima_venta_servida(request):
    venta = Venta.objects.order_by('-fecha_hora').first()

    if not venta:
        return Response(
            {"mensaje": "No hay ventas registradas"},
            status=status.HTTP_404_NOT_FOUND
        )

    if venta.servido:
        return Response(
            {"mensaje": "La última venta ya está marcada como servida"},
            status=status.HTTP_400_BAD_REQUEST
        )

    venta.servido = True
    venta.save()

    return Response({
        "mensaje": "Venta marcada como servida",
        "venta_id": venta.id
    })

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
        
    })"""


