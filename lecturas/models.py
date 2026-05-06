from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
    

class Venta(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)

    

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
   
