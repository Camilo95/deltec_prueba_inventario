import uuid

from django.db import models

# Create your models here.
class persona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    identificacion = models.CharField(max_length=20, unique=True, null=False, blank=False)
    nombres = models.CharField(max_length=400, null=False, blank=False)
    apellidos = models.CharField(max_length=400, null=False, blank=False)


    def __str__(self):
        txt = "Usuario: {0}, Identificación ({1})"
        return txt.format(self.nombre_completo(), self.identificacion)

    def nombre_completo(self):
        txt = "{0} {1}"
        return txt.format(self.apellidos, self.nombres)