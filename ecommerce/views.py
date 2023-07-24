
from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('produtos')
            
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

def categoria_criar(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('categorias')
            
    else:
        form = CategoriaForm()

    return render(request, "ecommerce/categoria.html", {'form': form})

def produto_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produtos = Produto.objects.all()
    
    context = {
        'produto': produto,
        'produtos': produtos
    }

    return render(request, 'ecommerce/detail_product.html', context)

def categoria_detalhes(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    produtos = Produto.objects.all()

    context = {
        'categoria': categoria,
        'produtos': produtos
    }

    return render(request, 'ecommerce/detail_categorias.html', context)

def produtos_por_departamento(request, departamento_id):
    departamento = get_object_or_404(Categoria, pk=departamento_id)
    produtos = Produto.objects.filter(categoria=departamento)

    context = {
        'departamento': departamento,
        'produtos': produtos,
    }

    return render(request, 'ecommerce/produtos_por_departamentos.html', context)

