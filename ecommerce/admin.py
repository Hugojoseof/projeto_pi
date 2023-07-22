from django.contrib import admin
from .models import Categoria,Pessoa,Produto
# Register your models here.

@admin.register(Categoria)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_categoria',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display= ('nome_produto', )

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome')
