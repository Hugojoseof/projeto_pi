from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Categoria,Produto,Pessoa
from .forms import ProdutoForm, CategoriaForm
# Create your views here.

def index (request):
    categoria  = Categoria.objects.all()
    produto = Produto.objects.all()

    context = {
        'categorias': categoria,
        'produtos': produto,
    }
    return render (request, "ecommerce/index.html", context)

def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect('index')
            
    else:
        form = ProdutoForm()

    return render(request, "ecommerce/produto.html", {'form': form})

def admin_pag(request): 
    return render(request,"ecommerce/adm.html")

def produtos(request):
    produto = Produto.objects.all()

    context = {
        'produtos': produto,
    }
    return render (request, "ecommerce/produtosgerais.html", context)

def categorias(request):
    categoria = Categoria.objects.all()

    context = {
        'categorias': categoria,
    }
    return render (request, "ecommerce/categoriasgerais.html", context)

