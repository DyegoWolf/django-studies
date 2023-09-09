from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=400)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')

    # Método que define as colunas que serão apresentadas na tabela do painel administrativo
    def __str__(self):
        return (self)

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=400)
    sobrenome = models.CharField('Sobrenome', max_length=400)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return (self.nome)