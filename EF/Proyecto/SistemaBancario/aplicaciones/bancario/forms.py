from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import users
from .models import Usuarios

class Registro(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['User_Nombre', ' User_Apellidos', 'User_Cedula', 'User_Tel', 'User_Direccion', 'User_Email', 'User_Passwd']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['User_Nombre', ' User_Apellidos', 'User_Cedula', 'User_Tel', 'User_Direccion', 'User_Email', 'User_Passwd']

