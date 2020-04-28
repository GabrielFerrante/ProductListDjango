#CASO SUA APLICAÇÃO PRECISE DE FORMULÁRIOS
#DEVE-SE CRIAR UM ARQUIVO FORMS.PY


from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto

#Forms para integrar com BD
class ProdutoModelForm(forms.ModelForm):
    #Meta dados
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']

#Forms que não possuem integração com BD
class contactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    about = forms.CharField(label='Assunto', max_length=120)
    #Usando charfield só que com espaço de text area
    message = forms.CharField(label='Messagem', widget= forms.Textarea())

    
    def send_mail(self):
        nome = self.cleaned_data['name']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['about']
        mensagem = self.cleaned_data['message']

        conteudo = f'Nome {nome}\nE-mail {email}\nAssunto {assunto}\nMensagem {mensagem}'
        #Cria um objeto de mensagem de email
        em = EmailMessage(
            subject='E-mail enviado pelo sistema Projeto2',
            body=conteudo,
            #De
            from_email='contato@dominio.com.br',
            #Para
            to=['gabrielsferrante@hotmail.com'],
            headers={'Reply-To' : email}
        )
        em.send()