from django.contrib import admin

# Register your models here.
from .models import Produto

#Decorator para registrar a model no admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo']