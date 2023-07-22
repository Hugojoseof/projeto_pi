from django.db import models

# Create your models here.

class Categoria (models.Model):
    nome_categoria = models.CharField(max_length=100)
    imagem_categoria = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.nome_categoria
    
class Produto(models.Model):
    nome_produto = models.CharField( max_length=100)
    valor = models.IntegerField()
    descricao = models.TextField()
    imagem_principal = models.ImageField()
    imagem_1 = models.ImageField()
    imagem_2 = models.ImageField()
    imagem_3 = models.ImageField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_produto

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
