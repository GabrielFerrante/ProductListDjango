from django.db import models

# Create your models here.

from stdimage.models import StdImageField

#SIGNALS
#Serve para fazer operações antes e/ou após persistencia de dados
from django.db.models import signals
#Cria uma url valida a partir de um texto
from django.template.defaultfilters import slugify

#Classe abstrata para servir como base para outras models do projeto
class Base(models.Model):
    #Campos em comum para todas as models
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo ?', default=True )

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome do Produto', max_length=100)
    #Obrigatorio o numero maximo de digitos antes da virgula e quantas casas decimais
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    estoque = models.IntegerField('Estoque')

    #variations define um tamanho padrão de imagem e cria uma variação da mesma imagem upada
    imagem = StdImageField('Imagem',upload_to='produtos', variations={'thumb':(124,124)})

    #Pode ser nulo e não editavel
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def produto_pre_save(signal, instance, sender, **kwargs):
    #Gera um a slug com o nome do produto tudo minusculo e com traço
    #Exemplo: nome = Maria Mole --->> slug = maria-mole
    instance.slug = slugify(instance.nome)

#Antes de salvar, executa a função produto_pre_save
#quando a classe Produto, submeter um sinal
signals.pre_save.connect(produto_pre_save, sender=Produto)