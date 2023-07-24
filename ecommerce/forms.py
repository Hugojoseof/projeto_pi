from django.forms import ModelForm
from django import forms
from .models import Categoria,Produto,Pessoa

class CategoriaForm(ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nome_categoria' : forms.TextInput(attrs={'class': 'form-control' }),
            'imagem_categoria' :forms.FileInput(attrs={'class': 'form-control'}),
        }

class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome_produto' : forms.TextInput(attrs={'class': 'form-control' }),
            'valor' : forms.NumberInput(attrs={'class': 'form-control' }),
            'decricao' : forms.Textarea(attrs={'class': 'form-control' }),
            'imagem_principal' : forms.FileInput(attrs={'class': 'form-control'}),
            'imagem_1' : forms.FileInput(attrs={'class': 'form-control'}),
            'imagem_2': forms.FileInput(attrs={'class': 'form-control'}),
            'imagem_3' : forms.FileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control' })
        }