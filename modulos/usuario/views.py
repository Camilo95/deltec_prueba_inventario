from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView
from modulos.usuario.models import persona
from modulos.inventario.models import asignado
from modulos.usuario.forms import FormPersona, FormEditPersona



decorators = [never_cache, login_required]

class home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Pagina Principal"

        return context


class lista_personas(ListView):
    model = persona
    template_name = "lista_persona.html"
    context_object_name = 'personas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Lista de personas"
        return context
    
    def get_queryset(self):

        try:
            # Consulta todas las personas
            personas = persona.objects.all()

            # Consulta y cuenta todos los recursos que estan asignados por cada persona
            for x in personas:
                x.recursos_asignados = asignado.objects.filter(persona_id = x.id).filter(fecha_desvinculacion__isnull=True).count()

        except persona.DoesNotExist:
            personas = None
            return redirect('home')


        return personas


class detalle_persona(ListView):
    model = persona
    template_name = "detalle_persona.html"
    context_object_name = 'persona'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle de persona"

        return context
    
    
    def get_queryset(self):

        id = self.kwargs.get('id',None)

        try:
            # consulta una perosna por numero de identificacion
            query = persona.objects.get(identificacion=id)
        except persona.DoesNotExist:
            query = None
            return redirect('lista_personas')


        return query


class editar_persona(UpdateView):
    model = persona
    form_class = FormEditPersona
    template_name = "editar_persona.html"
    success_url = reverse_lazy("lista_personas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Persona"

        return context
    
    def form_valid(self, form):
        return super().form_valid(form)


class registro_persona(CreateView):
    model = persona
    template_name = "crear_persona.html"
    form_class = FormPersona
    success_url = reverse_lazy("lista_personas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Registro Persona"

        return context
