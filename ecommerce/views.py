from django.shortcuts import render
from .models import Categoria,Produto,Pessoa
# Create your views here.

def index (request):
    categoria  = Categoria.objects.all()
    produto = Produto.objects.all()

    context = {
        'categorias': categoria,
        'produtos': produto,
    }
    return render (request, "ecommerce/index.html", context)
