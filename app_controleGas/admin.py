from django.contrib import admin
from .models import Apartamento, Leitura 

@admin.register(Apartamento)
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('apartamento', 'ativo', 'criado', 'atualizado')

@admin.register(Leitura)
class LeituraAdmin(admin.ModelAdmin):
    list_display = ('apartamento', 'leitura', 'mes', 'data', 'ativo', 'atualizado')