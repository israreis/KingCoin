<<<<<<< HEAD
#Arquivo de rotas
=======
#arquivo de rotas do projeto
>>>>>>> 109d6de (adicionando a landing page)

from django.contrib import admin
from django.urls import path
from financas.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),  # raiz do site aponta para landing
]