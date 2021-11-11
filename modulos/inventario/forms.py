from django import forms
from .models import asignado, recurso


class FormRecurso(forms.ModelForm):
    class Meta:
        model = recurso
        fields = ('codigo','nombre','serial','categoria','marca')
        labels = {
            'codigo':'Codigo',
            'nombres': 'Nombre',
            'serial': 'Serial',
            'categoria':'Categoria',
            'marca':'Marca'
        }
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'',
                    'id':'identificacion'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'',
                    'id':'nombres'
                }
            ),
            'serial': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'',
                    'id':'apellidos'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'',
                    'id':'apellidos'
                }
            ),
            'marca': forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'',
                    'id':'apellidos'
                }
            )
        }


class FormRecursoDesvinculacion(forms.ModelForm):

    class Meta:
        model = asignado
        fields = ('fecha_desvinculacion'),
        labels = {
            'fecha_desvinculacion':'Fecha de desvinculación'
        }
        widgets = {
            'fecha_desvinculacion': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'hidden':True
                })
        }


class FormCrearAsignacionSinCodigo(forms.ModelForm):

    class Meta:
        model = asignado
        fields = ('recurso','persona')
        labels = {
            'recurso':'Recurso',
            'persona': 'Persona'
        }
        widgets = {
            'recurso': forms.Select(
                attrs={
                    'class':'form-control',
                    
                }
            ),
            'persona': forms.Select(
                attrs={
                    'class':'form-control'
                }
            )
        }


class FormCrearAsignacion(forms.ModelForm):

    class Meta:
        model = asignado
        fields = ('recurso','persona')
        labels = {
            'recurso':'Recurso',
            'persona': 'Persona'
        }
        widgets = {
            'recurso': forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
            'persona': forms.Select(
                attrs={
                    'class':'form-control'
                }
            )
        }