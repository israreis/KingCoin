from django.contrib import admin
from django.urls import path, include
from financas.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('financas.urls')),  
    path('financas/', include('financas.urls')),  
]
