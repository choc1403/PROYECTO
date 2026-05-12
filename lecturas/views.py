from django.shortcuts import render

from .models import ProductoServido, Venta, DetalleVenta

# Create your views here.

def crear_venta(datos):
    venta = Venta.objects.create()

    for item in datos:
        producto = ProductoServido.objects.get(id=item['producto_id'])

        if producto.stock < item['cantidad']:
            raise Exception("No hay suficiente stock")

        DetalleVenta.objects.create(
            venta=venta,
            producto=producto,
            cantidad=item['cantidad']
        )

        # actualizar stock
        producto.stock -= item['cantidad']
        producto.save()

    return venta