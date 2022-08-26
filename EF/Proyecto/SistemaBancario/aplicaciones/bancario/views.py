from contextlib import redirect_stderr
from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from aplicaciones.users.models import *
from aplicaciones.cuentas.models import *
from django.contrib import messages
from datetime import datetime
import time



def index(request):
    return render(request, 'index.html')

def login(request):
     return render(request, 'login.html')

def signup(request):  
    return render(request, 'signup.html')

def registro(request):   
    User_Nombre = request.POST['Nombre']
    User_Apellidos = request.POST['Apellido']
    User_Cedula = request.POST['Cedula']
    User_Tel = request.POST['Telefono']
    User_Direccion = request.POST['Direccion']
    User_Email = request.POST['CorreoElectrónico']
    User_Passwd = request.POST['loginPassword']
    cu_TP = request.POST['TipodeCuenta']
    fecha = str(datetime.today().strftime('%Y-%m-%d'))

    try:
        usuario = Usuarios.objects.get(User_Cedula=User_Cedula) 
        messages.error(request, "Esta Cédula ya se encuentra asociada a una Cuenta. Inténtelo de Nuevo." )
        return redirect('/signup.html')

    except Usuarios.DoesNotExist as e1:
        usuarios = Usuarios.objects.create(User_Nombre=request.POST.get(User_Nombre,User_Nombre), User_Apellidos=request.POST.get(User_Apellidos,User_Apellidos), 
          User_Cedula=request.POST.get(User_Cedula,User_Cedula), User_Tel=request.POST.get(User_Tel,User_Tel), User_Direccion=request.POST.get(User_Direccion,User_Direccion), 
          User_Email=request.POST.get(User_Email,User_Email), User_Passwd=request.POST.get(User_Passwd,User_Passwd), User_Status=request.POST.get(User_Nombre,'A'))
          
        cuenta = Cuentas.objects.create(CU_CEDULACLI=request.POST.get(User_Cedula,User_Cedula), CU_FECHAPERTURA= fecha, CU_SALDO=request.POST.get(100,100),
          CU_TP =request.POST.get(cu_TP,cu_TP), CU_STATUS=request.POST.get(User_Nombre,'A'))
        
    return redirect('/index.html')



def iniciar(request):
    User_Cedula = request.POST['Cedula']
    User_Passwd = request.POST['pass']

    if request.method=='POST':
        try:
            usuario = Usuarios.objects.get( User_Cedula=request.POST.get(User_Cedula,User_Cedula), 
             User_Passwd=request.POST.get(User_Passwd,User_Passwd)) 

            request.session['User_Email']=usuario.User_Email
            request.session['User_Nombre']=usuario.User_Nombre
            request.session['User_Apellidos']=usuario.User_Apellidos
            request.session['User_Cedula']=usuario.User_Cedula
            request.session['User_Direccion']=usuario.User_Direccion
            request.session['User_Tel']=usuario.User_Tel
            User_Cedula = request.session['User_Cedula']

            cuenta = Cuentas.objects.get(CU_CEDULACLI=User_Cedula) 
            request.session['CU_SALDO']=cuenta.CU_SALDO
            return redirect('/Principal_Cli.html')

        except Usuarios.DoesNotExist as e1:
            messages.error(request, "Cédula o Password Incorrecto." )
            return redirect('/login.html')

        except Usuarios.MultipleObjectsReturned as e2:
            messages.error(request, "Existe más de una cuenta con esta cedula." )
            return redirect('/login.html')
            
    return render(request,'/login.html')
    


def CerrarSesion(request):
    try:
        del request.session['User_Email']
        del request.session['User_Nombre']
        del request.session['User_Apellidos']
        del request.session['User_Cedula']
        del request.session['User_Direccion']
        del request.session['User_Tel']
        del request.session['CU_SALDO']
    except:
        return redirect('/index.html')
            
    return redirect('/index.html')



def eliminarCuenta(request):
    User_Cedula = request.session['User_Cedula']
    try:
        usuario = Usuarios.objects.filter(User_Cedula=User_Cedula) 
        usuario.delete()
        cuenta = Cuentas.objects.filter(CU_CEDULACLI=User_Cedula) 
        cuenta.delete()
        messages.error(request, "Se ha eliminado la cuenta y el usuario" )
        return redirect('/login.html')

    except Usuarios.DoesNotExist as e1:
        messages.error(request, "Error al eliminar usuario." )
        return redirect('/Principal_Cli.html')
        


def update(request):
    User_Nombre = str(request.POST['firstName'])
    User_Apellidos = request.POST['fullName']
    User_Direccion = request.POST['address']
    User_Cedula = request.session['User_Cedula']

    try:
        usuario = Usuarios.objects.filter(User_Cedula=User_Cedula) 
        usuarioss = Usuarios.objects.update(User_Nombre=request.POST.get(User_Nombre,User_Nombre), User_Apellidos=request.POST.get(User_Apellidos,User_Apellidos),
         User_Direccion=request.POST.get(User_Direccion,User_Direccion))

        messages.error(request, "Se han actualizado sus datos personales. Inicie Sesión." )
        return redirect('/login.html')

    except Usuarios.DoesNotExist as e1:
        messages.error(request, "Error al Actualizar Datos." )
        return redirect('/index.html')



def update1(request):
     User_Email = request.POST['emailID']
     User_Cedula = request.session['User_Cedula']
    
     try:
         usuario = Usuarios.objects.filter(User_Cedula=User_Cedula) 
         usuarioss = Usuarios.objects.update (User_Email=request.POST.get(User_Email,User_Email))

         messages.error(request, "Se ha actualizado su Email. Inicie Sesión." )
         return redirect('/login.html')
        
     except Usuarios.DoesNotExist as e1:
        messages.error(request, "Error al Actualizar Datos." )
        return redirect('/index.html')



def update2(request):
    User_Tel = request.POST['mobileNumber']
    User_Cedula = request.session['User_Cedula']
    
    try:
         usuario = Usuarios.objects.filter(User_Cedula=User_Cedula) 
         usuarioss = Usuarios.objects.update (User_Tel=request.POST.get(User_Tel,User_Tel))
         messages.error(request, "Se ha actualizado su numero de teléfono. Inicie Sesión." )
         return redirect('/login.html')
        
    except Usuarios.DoesNotExist as e1:
        messages.error(request, "Error al Actualizar Datos." )
        return redirect('/index.html')


def update3(request):
    User_Passwd = request.POST['newPassword']
    User_Cedula = request.session['User_Cedula']
    
    try:
         usuario = Usuarios.objects.filter(User_Cedula=User_Cedula) 
         usuarioss = Usuarios.objects.update (User_Passwd=request.POST.get(User_Passwd,User_Passwd))
         messages.error(request, "Se ha actualizado su contraseña. Inicie Sesión." )
         return redirect('/login.html')
        
    except Usuarios.DoesNotExist as e1:
        messages.error(request, "Error al Actualizar Datos." )
        return redirect('/index.html')


def transactions_Cli(request):
    User_Cedula = request.session['User_Cedula']
    data2 = Transacciones.objects.filter(TRA_CEDULACLI = User_Cedula)
    info = {
        "TRA_FECHA": data2,
        "NUMEROTRANSACCION": data2,
        "TRA_CUENTABANC": data2,
        "TRA_MONTO": data2,
    }
    return render(request, 'transactions_Cli.html', info)



def Principal_Cli(request):
    User_Cedula = request.session['User_Cedula']
    data = Cuentas.objects.filter(CU_CEDULACLI = User_Cedula)
    balance = {"CU_SALDO": data}

    return render(request, 'Principal_Cli.html', balance)

    
def sendmoney_Cli(request):
    return render(request, 'send-money_Cli.html')

def aboutus(request):
    return render(request, 'about-us.html')

def help_Cli(request):
    return render(request, 'help_Cli.html')

def deposito(request):
    TRA_CUENTABANC = request.POST['cuentaDestino']
    TRA_MONTO = request.POST['montoTransaccion']
    User_Cedula = request.session['User_Cedula']
    
    cuenta = Cuentas.objects.get(CU_CEDULACLI = User_Cedula)
    request.session['CU_SALDO']=cuenta.CU_SALDO

    monTo= request.session['CU_SALDO']=cuenta.CU_SALDO
    TM = int(TRA_MONTO)

    monT0= int(monTo)
    balanceActualizado = monT0 - TM
    DepositO = Cuentas.objects.filter(CU_CEDULACLI = User_Cedula).update(CU_SALDO=request.POST.get(balanceActualizado,balanceActualizado))
    
    Deposito = Transacciones.objects.create(TRA_CUENTABANC =request.POST.get(TRA_CUENTABANC,TRA_CUENTABANC),
     TRA_MONTO=request.POST.get(TRA_MONTO,TRA_MONTO), TRA_CEDULACLI= request.POST.get(User_Cedula,User_Cedula))

    t = Cuentas.objects.get(NUMEROCUENTA=TRA_CUENTABANC)
    request.session['CU_SALDO'] = t.CU_SALDO
    monTo2 = request.session['CU_SALDO']=t.CU_SALDO
    monT02 = int(monTo2)
    newBalanceDestinatario = monT02 + TM
    Deposit0 = Cuentas.objects.filter(NUMEROCUENTA=TRA_CUENTABANC).update(CU_SALDO=request.POST.get(newBalanceDestinatario,newBalanceDestinatario))

    return redirect('/transactions_Cli.html')