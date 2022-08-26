from django.contrib import admin
from django.urls import path, include
from aplicaciones.bancario.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('index.html', index),
    path('login.html', login),
    path('signup.html',signup),

    path('iniciar/',iniciar),
    path('registro/',registro),
    path('CerrarSesion/', CerrarSesion),
    path('eliminarCuenta/', eliminarCuenta),
    path('update/', update),
    path('update1/', update1),
    path('update2/', update2),
    path('update3/', update3),

    path('Principal_Cli.html',Principal_Cli),
    path('transactions_Cli.html',transactions_Cli),
    path('send-money_Cli.html',sendmoney_Cli),
    path('about-us.html',aboutus),
    path('help_Cli.html',help_Cli),

    path('deposito/', deposito),
]
