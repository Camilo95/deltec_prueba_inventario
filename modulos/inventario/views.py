from datetime import datetime
from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import recurso, marca, categoria, asignado
from modulos.usuario.models import persona
from .forms import FormRecurso, FormCrearAsignacion, FormRecursoDesvinculacion, FormCrearAsignacionSinCodigo


class lista_recursos(ListView):
    model = recurso
    template_name = "lista_recursos.html"
    context_object_name = 'recursos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Lista de recursos"

        return context

    def get_queryset(self):

        try:
            # Consulta todo los recursos
            recursos = recurso.objects.all()

            # Itera en todos los registros de la tabla recurso
            for x in recursos:
                
                # Filtra el recurso en la tabla de asignacion
                asignacion = asignado.objects.filter(recurso_id = x.id).filter(fecha_desvinculacion__isnull = True)
                
                #Valida que exista 1 solo registro
                if len(asignacion) == 1 :
                    
                    # Obtiene el nombre completo de la persona asociada al recurso
                    x.persona_asignada = asignacion[0].persona.nombre_completo()

                    # Asigna el id del registro de asignacion
                    x.asignado_id = asignacion[0].id
                else:
                    # Asigna el siguiente mensaje indicando que el recurso esta disponible
                    x.persona_asignada = "Sin asignación"


        except recurso.DoesNotExist:
            recursos = None
            return redirect('lista_recursos')


        return recursos


class lista_asignaciones_personas(ListView):
    model = asignado
    template_name = "lista_asignaciones.html"
    context_object_name = 'asignaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Lista de asignaciones"
        context['identificacion_persona'] = self.kwargs.get('id',None)

        return context

    def get_queryset(self):

        #Identificacion de la persona
        id = self.kwargs.get('id',None)

        try:
            #Consulta la persona por su identificación
            usuario = persona.objects.get(identificacion = id)

            #Lista de recursos asignados a la persona consultada
            recursos_asignados = asignado.objects.filter(persona_id = usuario.id).filter(fecha_desvinculacion__isnull=True)

        except recurso.DoesNotExist:
            #Devuelve None cuando no hay listado
            recursos_asignados = None
            return redirect('lista_recursos')

        return recursos_asignados


class lista_asignaciones(ListView):
    model = asignado
    template_name = "lista_asignaciones.html"
    context_object_name = 'asignaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Lista de asignaciones"
        context['identificacion_persona'] = self.kwargs.get('id',None)

        return context

    def get_queryset(self):
        query = asignado.objects.filter(fecha_desvinculacion=None)

        return query


class historial_asignaciones(ListView):
    model = asignado
    template_name = "lista_asignaciones.html"
    context_object_name = 'asignaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Lista de asignaciones"
        context['identificacion_persona'] = self.kwargs.get('id',None)

        return context

    def get_queryset(self):
        # consulta todos los asingados que tenga fecha de desvinculacion en null
        query = asignado.objects.filter(fecha_desvinculacion__isnull=False)

        return query


class historial_asignaciones_persona(ListView):
    model = asignado
    template_name = "lista_asignaciones.html"
    context_object_name = 'asignaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Lista de asignaciones"
        context['identificacion_persona'] = self.kwargs.get('id',None)

        return context

    def get_queryset(self):
        
        identificacion = self.kwargs.get('id',None)

        #colsulta una sola persona para obtener el pk
        persona_object = persona.objects.get(identificacion = identificacion)

        #consulta todos las asignaciones asociadas al pk de la persona con fecha de desvinculacion no null
        query = asignado.objects.filter(persona = persona_object.id).filter(fecha_desvinculacion__isnull=False)

        return query


class detalle_asignacion(UpdateView):
    model = asignado
    form_class = FormRecursoDesvinculacion
    template_name = "detalle_asignacion.html"
    context_object_name = 'asignado_object'
    success_url = reverse_lazy("lista_asignaciones")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle de recurso"
        context['pk'] = self.kwargs.get('pk',None)

        return context


class detalle_recurso(ListView):
    model = recurso
    template_name = "detalle_recurso.html"
    context_object_name = 'recurso'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle de recurso"

        return context
    
    
    def get_queryset(self):

        recurso_codigo = self.kwargs.get('codigo',None)

        try:
            #consulta un recurso por medio de codio interno
            query = recurso.objects.get(codigo=recurso_codigo)
        except recurso.DoesNotExist:
            query = None
            return redirect('lista_recursos')


        return query


class registro_recurso(CreateView):
    model = recurso
    template_name = "crear_recurso.html"
    form_class = FormRecurso
    success_url = reverse_lazy("lista_recursos")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Registro Recurso"
        context['marcas'] = marca.objects.all()
        context['categoria'] = categoria.objects.all()

        return context
    

class editar_recurso(UpdateView):
    model = recurso
    form_class = FormRecurso
    template_name = "editar_recurso.html"
    success_url = reverse_lazy("lista_recursos")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Recurso"
        context['codigo'] = recurso.objects.get(pk=self.kwargs.get('pk',None)).codigo

        return context


class crear_asignacion(CreateView):
    model = asignado
    template_name = "asignar_recurso.html"
    form_class = FormCrearAsignacion
    success_url = reverse_lazy("lista_recursos")

    def custom_form(self):
        """ formulario perosnalizado """
        try:
            recurso_codigo = self.kwargs.get('codigo',None)
            recurso_object = recurso.objects.get(codigo = recurso_codigo)
            form = self.form_class(initial = {'recurso': recurso_object})
            recursos_disponibles = recurso.objects.filter(es_asignado = False)
            form.fields["recurso"].queryset = recursos_disponibles
            return form            
        except recurso.DoesNotExist:
            form = self.form_class()
            recursos_disponibles = recurso.objects.filter(es_asignado = False)
            form.fields["recurso"].queryset = recursos_disponibles
            
            return form


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Registro Asignación"
        context['codigo_recurso'] = self.kwargs.get('codigo',None)
        context['form'] = self.custom_form()

        return context

    def update_recurso(self):
        recurso_codigo = self.kwargs.get('codigo',None)
        recurso_object = recurso.objects.get(codigo = recurso_codigo)
        recurso_object.es_asignado = True
        recurso_object.save()

    def form_valid(self, form):
        self.update_recurso()

        return super().form_valid(form)


class crear_asignacion_sin_codigo(CreateView):
    model = asignado
    template_name = "asignar_recurso_sin_codigo.html"
    form_class = FormCrearAsignacionSinCodigo
    success_url = reverse_lazy("lista_recursos")

    def custom_form(self):
        try:
            form = self.form_class()
            recursos_disponibles = recurso.objects.filter(es_asignado = False)
            form.fields["recurso"].queryset = recursos_disponibles

            return form            
        except recurso.DoesNotExist:
            return self.form_class


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Registro Asignación"
        context['codigo_recurso'] = "Opcion libre"
        context['form'] = self.custom_form()

        return context

    def form_valid(self, form):
        recurso_codigo = self.request.POST['recurso']
        recurso_object = recurso.objects.get(pk = recurso_codigo)
        recurso_object.es_asignado = True
        recurso_object.save()

        return super().form_valid(form)


class desvincular_asignacion(UpdateView):
    model = asignado
    form_class = FormRecursoDesvinculacion
    template_name = "editar_asignacion.html"
    context_object_name = 'asignado_object'
    success_url = reverse_lazy("lista_asignaciones")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Desvincular Recurso"
        context['pk'] = self.kwargs.get('pk',None)
        context['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return context

    def get_url_redirect(self):
        return self.request.GET['page']

    def desvincular_asignacion(self, asignado_object ):
        recurso_object = asignado_object.recurso
        recurso_object.es_asignado = False
        recurso_object.save()

    def get_asignacion(self):
        pk = self.kwargs.get('pk',None)
        asignado_object = asignado.objects.get(pk=pk)
        return asignado_object
    
    def form_valid(self, form):
        super().form_valid(form)
        asignacion_object = self.get_asignacion()
        self.desvincular_asignacion(asignacion_object)
        return redirect(self.get_url_redirect())

