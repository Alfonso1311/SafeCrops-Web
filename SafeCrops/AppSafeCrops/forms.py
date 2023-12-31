from typing import Any, Dict
from django import forms
from django.contrib.auth.hashers import make_password
from django.core.validators import FileExtensionValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Administrador, Experto, Tester, Enfermedad, Dataset, Cultivo, Modelo

'''
Se crea los formularios a partir de los campos que se encuentran en los modelos o creando 
nuevos campos haciendo uso de los widgets de django
'''

class TempUsuario(forms.ModelChoiceField): # Se crea una clase para el campo de tipo ModelChoiceField
    def label_from_instance(self, obj): # Se define el método label_from_instance
        return str(obj.id)+" - "+str(obj.username) # Se retorna el valor que se va a mostrar en el campo


class AdministradorForm(forms.ModelForm, forms.Form):  # Formulario para el modelo Administrador
    #user = TempUsuario(queryset=User.objects.all().order_by('-id'), label=None, widget=forms.Select(attrs={'class':'form-select'}), required=True) # Se crea un campo de tipo ModelChoiceField

    class Meta: # Se define la clase Meta
        model = Administrador # Se define el modelo
        fields = ['id_Administrador', 'nombre', 'apellidoP', 'apellidoM', 'fechaNac', 'correo', 'imagen', 'userType'] # Se definen los campos que se van a mostrar en el formulario


class ExpertoForm(forms.ModelForm, forms.Form): # Formulario para el modelo Experto
    #user = TempUsuario(queryset=User.objects.all().order_by('-id'), label=None, widget=forms.Select(attrs={'class':'form-select'}), required=True) # Se crea un campo de tipo ModelChoiceField

    class Meta: # Se define la clase Meta 
        model = Experto # Se define el modelo
        fields = ['nombre', 'apellidoP', 'apellidoM', 'fechaNac', 'correo', 'institucionPerteneciente', 'imagen', 'userType']  # Se definen los campos que se van a mostrar en el formulario


class TesterForm(forms.ModelForm): # Formulario para el modelo Tester
    #user = TempUsuario(queryset=User.objects.all().order_by('-id'), label=None, widget=forms.Select(attrs={'class':'form-select'}), required=True) # Se crea un campo de tipo ModelChoiceField

    class Meta: # Se define la clase Meta
        model = Tester # Se define el modelo
        fields = ['nombre', 'apellidoP', 'apellidoM', 'fechaNac', 'correo', 'imagen', 'userType'] # Se definen los campos que se van a mostrar en el formulario


class UsuarioForm(UserCreationForm, forms.ModelForm): # Formulario para el modelo Usuario
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'})) # Se define el campo password1
    password2: forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'})) # Se define el campo password2
   
    class Meta: # Se define la clase Meta
        model = User # Se define el modelo
        fields = ['username', 'password1', 'password2'] # Se definen los campos que se van a mostrar en el formulario


class ResetPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'autocomplete': 'on',
        'autofocus': True
    }))

class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'autocomplete': 'off',
        'autofocus': True
    }))

    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'autocomplete': 'off'
    }))

class EnfermedadForm(forms.ModelForm):
    cultivoEnfermedad = forms.ModelChoiceField(queryset=Cultivo.objects.all().order_by('-id_Cultivo'), label=None, widget=forms.Select(attrs={'class':'form-select'}), required=True) # Se crea un campo de tipo ModelChoiceField
    
    class Meta:
        model = Enfermedad
        fields = '__all__'

class DatasetForm(forms.ModelForm):
    ruta = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    class Meta:
        model = Dataset
        fields = '__all__'

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = '__all__'

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'