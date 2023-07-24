
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
    produtos = Produto.objects.all()

    context = {
        'produto': produtos,
    }
    return render(request,"ecommerce/adm.html",context)

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

def produto_detalhes(request, id):
    produto = get_object_or_404(Produto, id=id)
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


def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect("pag_admin")
def editar_produto(request,id):
    produto = get_object_or_404(Produto,id=id)
    forms = ProdutoForm(instance=produto)

    if(request.method == 'POST'):
        forms = ProdutoForm(request.POST, instance=produto)
        if(forms.is_valid()):
            produto.save()
            return redirect('pag_admin')
        else:
            return render(request, 'ecommerce/edit.html', { 'form':forms, 'produtos':produto } )
    else:
        return render(request, 'ecommerce/edit.html', { 'form':forms, 'produtos':produto } )