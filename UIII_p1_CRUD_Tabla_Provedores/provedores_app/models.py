from django.db import models

# Create your models here.

class Provedores(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    numero=models.CharField(max_length=15)
    direccion=models.CharField(max_length=50)
    idproductos=models.CharField(max_length=25)
    Precio=models.CharField(max_length=100)
    marca=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.id