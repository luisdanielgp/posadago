from django.contrib import admin
from .models import Posada, Asistente

# Register your models here.


class PosadaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Posada, PosadaAdmin)


class AsistenteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Asistente, AsistenteAdmin)
