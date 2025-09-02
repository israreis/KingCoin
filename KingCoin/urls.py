#arquivo de rotas do projeto

from django.contrib import admin
from django.urls import path
from financas.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),  # raiz do site aponta para landing
]