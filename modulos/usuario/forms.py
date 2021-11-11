from django import forms
from .models import persona


class FormPersona(forms.ModelForm):
    class Meta:
        model = persona
        fields = ('identificacion','nombres','apellidos')
        labels = {
            'identificacion':'Identificación',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos'
        }
        widgets = {
            'identificacion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'1113677400',
                    'id':'identificacion'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'',
                    'id':'nombres'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'',
                    'id':'apellidos'
                }
            )
        }


class FormEditPersona(forms.ModelForm):
    class Meta:
        model = persona
        fields = ('identificacion','nombres','apellidos')
        labels = {
            'identificacion':'Identificación',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos'
        }
        widgets = {
            'identificacion': forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            )
        }