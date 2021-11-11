from django.urls import path

from .views import *

urlpatterns = [
    path('', lista_recursos.as_view(), name="lista_recursos"),
    path('<int:codigo>/', detalle_recurso.as_view(), name="detalle_recurso"),
    path('crear/', registro_recurso.as_view(), name="crear_recurso"),
    path('editar/<pk>/', editar_recurso.as_view(), name="editar_recurso"),
    path('asignaciones/', lista_asignaciones.as_view(), name="lista_asignaciones"),
    path('asignados/<int:id>', lista_asignaciones_personas.as_view(), name="lista_asignaciones"),
    path('crear/asignacion/<int:codigo>/', crear_asignacion.as_view(), name="crear_asignacion"),
    path('crear/asignacion/', crear_asignacion_sin_codigo.as_view(), name="crear_asignacion_sin_codigo"),
    path('editar/asignacion/persona/<pk>/', desvincular_asignacion.as_view(), name="desvincular_asignacion"),
    path('historial/asignaciones/', historial_asignaciones.as_view(), name="historial_asignaciones"),
    path('historial/asignaciones/<id>/', historial_asignaciones_persona.as_view(), name="historial_asignaciones_persona"),
    path('detalle/asignacion/<pk>/', detalle_asignacion.as_view(), name="detalle_asignacion")
    
]