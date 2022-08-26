from django.contrib import admin
from .models import TipoCuenta
from .models import Cuentas
from .models import Transacciones

admin.site.register(TipoCuenta)
admin.site.register(Cuentas)
admin.site.register(Transacciones)