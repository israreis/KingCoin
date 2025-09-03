#arquivo de rotas do projeto

from django.contrib import admin
from django.urls import path, include   # <-- precisa importar include
from financas.views import landing, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),  
    path("financas/", include("financas.urls")),  
]
