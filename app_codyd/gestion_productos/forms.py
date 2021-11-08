from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets,ModelChoiceField
from gestion_productos.models import Contacto, TipoContacto, Inventario

class ContactoForm(forms.ModelForm):
    tipo_contacto = forms.ModelChoiceField(queryset=TipoContacto.objects.all())
    class Meta:
        model = Contacto
        fields = ['nombre','apellido','direccion','email','cedula_nit']
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'cedula_nit': forms.TextInput(attrs={'class': 'form-control'}),
        
        }
        
class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "My este #%i" % obj.id

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre','precio_unitario','cant_stock','descripcion']
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
        'cant_stock': forms.NumberInput(attrs={'class': 'form-control'}),
        'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
                
        }

