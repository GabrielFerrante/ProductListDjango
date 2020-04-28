"""
WSGI config for projeto2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#Cling apresenta os arquivos staticos
#MediaCling apresenta arquivos de upload
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto2.settings')

application = Cling(MediaCling(get_wsgi_application()))
