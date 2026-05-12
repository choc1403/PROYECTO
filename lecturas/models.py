from django.db import models

# Create your models here.
class ProductoServido(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField(default=1)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    

class Venta(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    servido = models.BooleanField(default=False)

    

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(ProductoServido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
   
