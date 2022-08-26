from tkinter import CASCADE
from django.db import models

class Roles(models.Model):
    ROL_ID = models.IntegerField
    ROL_DESC_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Cliente', 'Cliente'),
    ]
    ROL_DESC = models.CharField(max_length= 25, choices= ROL_DESC_CHOICES)

    def __str__(self):
        return self.ROL_DESC

class Usuarios(models.Model):
    User_Cedula = models.CharField(max_length= 11, primary_key = True, blank=False)
    User_Nombre = models.CharField(max_length= 50)
    User_Apellidos = models.CharField(max_length= 50)
    User_Tel = models.CharField(max_length= 10)
    User_Direccion = models.CharField(max_length= 80)
    User_Email = models.EmailField(max_length= 70)
    User_Rol = models.ForeignKey(Roles,null=True,blank=True,on_delete= models.CASCADE)
    User_Passwd = models.CharField(max_length= 30)
    User_Status = models.CharField(max_length= 1)

    def __str__(self):
        return self.User_Cedula