from django.contrib import admin
from .models import Usuarios
from .models import Roles

admin.site.register(Usuarios)
admin.site.register(Roles)