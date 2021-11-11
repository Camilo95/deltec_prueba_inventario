import uuid

from django.db import models
from modulos.usuario.models import persona

# Create your models here.

class categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=500, null=False, blank=False, unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

class marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=500, null=False, blank=False, unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

class recurso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=50, null=False, blank=False, unique=True)
    nombre = models.CharField(max_length=1000, null=False, blank=False)
    serial = models.CharField(max_length=100, null=False, blank=False, unique=True)
    categoria = models.ForeignKey(categoria, models.RESTRICT)
    marca = models.ForeignKey(marca, models.RESTRICT)
    es_asignado = models.BooleanField(default=False, null=False)

    def __str__(self):
        txt = "Codigo({0}), {1} {2} {3}, serial({4})"
        return txt.format(self.codigo, self.categoria, self.marca, self.nombre, self.serial)

    def object(self):
        return {'id':self.id, 'nombre':self.__str__}


class asignado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_desvinculacion = models.DateTimeField(editable=True, null=True, blank=True)
    persona = models.ForeignKey(persona, models.RESTRICT)
    recurso = models.ForeignKey(recurso, models.RESTRICT)

    def __str__(self):
        txt = "Persona({0}), le asignarón ({1}), en la fecha({2})"
        return txt.format(self.persona, self.recurso, self.fecha_asignacion.strftime("%A %d/%m/%Y %H:%M:%S"))
