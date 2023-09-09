from django.contrib import admin
from .models import Cliente, Produto

# Classe que contém todos os atributos que serão listados na tabela do painel administrativo
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

# Arquivo para registro das models que serão listadas no painel administrativo
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
