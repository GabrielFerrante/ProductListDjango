from django.shortcuts import render
#Redirecionar para alguma url
from django.shortcuts import redirect

#Adicionar mensagens ao contexto da pagina
from django.contrib import messages

#Importando os forms
#Pego os models form para salvar dados
from .forms import contactForm, ProdutoModelForm

#recupero dados puxando do model
from .models import Produto

# Create your views here.
def index(request):

    context = {
        'produtos': Produto.objects.all()
    }

    return render(request,'index.html',context)
    
def contact(request):
    #Esse form pode ser vazio (no Get) quando o usuario só abrir a pagina 
    #ou conter dados (no Post) quando o usuario clicar no submit
    form = contactForm(request.POST or None)

    #Se ele foi preenchido
    if(request.method == 'POST'):
        #print(f'Post :{request.POST}')
        #verifica se o formulário é válido
        if form.is_valid():
            
            form.send_mail()

            messages.success(request, 'Enviado com sucesso')
            
            #limpando o formulário
            form = contactForm()
        else:
            messages.error(request, 'Erro ao enviar Email')

    context = {
        'form' : form
    }
    return render(request,'contato.html',context)

def product(request):

    print(f'{request.user}')

    if str(request.user) != 'AnonymousUser':
        #Foi submetido o formulario atraves do methodo POST ?
        #Se sim
        #Cadastra o produto e emite uma mensagem
        if(str(request.method) == 'POST'):
            form = ProdutoModelForm(request.POST, request.FILES)
            if(form.is_valid()):
            
                form.save()
                
                messages.success(request, 'Produto cadastrado com sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao cadastrar produto')
        #Ele está vazio
        else:
            form = ProdutoModelForm()
        context = {
            'form':form
        }
        return render(request,'produto.html', context)
    else:
        return redirect(index)
    