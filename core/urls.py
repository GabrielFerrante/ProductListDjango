from django.urls import path
from .views import contact,index,product

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',index, name='index'),
    path('contato',contact, name='contact'),
    path('produto',product, name='product'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#Adiciona uma "rota" para arquivos staticos