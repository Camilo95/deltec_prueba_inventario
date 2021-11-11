from django.urls import path
from .views import *

urlpatterns = [
    path('', lista_personas.as_view(), name="lista_personas"),
    path('<int:id>/', detalle_persona.as_view(), name="detalle_persona"),
    path('crear/', registro_persona.as_view(), name="crear_persona"),
    path('editar/<pk>/', editar_persona.as_view(), name="editar_persona"),
    
]