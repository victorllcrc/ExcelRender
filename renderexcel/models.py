from django.db import models

# Create your models here.
class dato (models.Model):
    nombre= models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

    class Meta:
        verbose_name="Dato"
        verbose_name_plural= "Datos"

    def __str__(self):
        return self.nombre