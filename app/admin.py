from django.contrib import admin
from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'inventory')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'firstname', 'lastname', 'email')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
