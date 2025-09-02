#Views.py é o arquivo de lógica do projeto
from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html')
