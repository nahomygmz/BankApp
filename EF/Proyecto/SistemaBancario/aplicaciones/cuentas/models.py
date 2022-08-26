from pickle import FALSE
from tkinter import CASCADE
from django.db import models
from aplicaciones.users.models import Usuarios

class TipoCuenta(models.Model):
    TC_ID = models.IntegerField
    TC_DESC_CHOICES = [
        ('CC', "Cuenta Corriente"),
        ('CCC', "Cuenta con Chequera"),
        ('CA', "Cuenta de Ahorro"),
        ('CN', "Cuenta de Nómina"),
        ('CD',"Cuenta en Dólares"),
    ]
    TC_DESC = models.CharField(max_length= 25, choices= TC_DESC_CHOICES)

    def __str__(self):
        return self.TC_DESC

def __str__(self):
    return self.User_Cedula

class Cuentas(models.Model):
    NUMEROCUENTA = models.AutoField(auto_created=True, primary_key= True)
    CU_CEDULACLI = models.CharField(max_length= 11, blank=False)
    CU_FECHAPERTURA = models.DateField(auto_now=False)
    CU_SALDO = models.BigIntegerField(default= 100)
    CU_TP = models.CharField(max_length=50)
    CU_STATUS = models.CharField(max_length= 1, default= 'A')

    def __int__(self):
        return self.CU_SALDO
 
class Transacciones(models.Model):
    NUMEROTRANSACCION = models.AutoField(auto_created=False, primary_key= True)
    TRA_CUENTABANC = models.CharField(max_length=20)
    TRA_FECHA = models.DateField (auto_now=True)
    TRA_TIPO = models.CharField(max_length= 50, null=True)
    TRA_MONTO = models.BigIntegerField(default= 0)
    TRA_CEDULACLI = models.CharField(max_length= 11, blank=False)


