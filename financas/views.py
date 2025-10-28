from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError
from .models import Profile
from django.contrib.auth import login
from .forms import (
    CustomLoginForm,
    CustomUserCreationForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
)

# --- Login ---
class CustomLoginView(LoginView):
    template_name = "financas/login.html"
    authentication_form = CustomLoginForm

# --- Logout ---
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("landing")

def RegisterView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Criar usuário usando o email como username
            email = form.cleaned_data['email']
            
            try:
                # Verificação extra para garantir que o email não existe
                if User.objects.filter(username=email).exists():
                    form.add_error('email', 'Este e-mail já está cadastrado.')
                elif User.objects.filter(email=email).exists():
                    form.add_error('email', 'Este e-mail já está cadastrado.')
                else:
                    user = User.objects.create_user(
                        username=email,  # Usa o email como username
                        email=email,
                        password=form.cleaned_data['password1'],
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name']
                    )
                    
                    # Criar perfil com telefone
                    Profile.objects.create(
                        user=user,
                        phone=form.cleaned_data['phone']
                    )
                    
                    # Fazer login automaticamente
                    login(request, user)
                    messages.success(request, 'Cadastro realizado com sucesso!')
                    return redirect('landing')  # Corrigido: era 'lading', deve ser 'landing'
                    
            except IntegrityError as e:
                form.add_error('email', 'Erro ao criar conta. Este e-mail já pode estar em uso.')
                print(f"Erro de integridade: {e}")
                
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'financas/register.html', {'form': form})

# --- Landing page ---
def landing(request):
    return render(request, "financas/landing.html")

# --- Recuperação de senha ---
class CustomPasswordResetView(PasswordResetView):
    template_name = "financas/password_reset.html"
    email_template_name = "financas/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")
    form_class = CustomPasswordResetForm

# --- Redefinir senha (nova senha) ---
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "financas/password_reset_confirm.html"
    success_url = reverse_lazy("login")
    form_class = CustomSetPasswordForm
  
# --- Tela de Transaçoes ---
def transacoes(request):
    return render(request, "financas/transacoes.html")

def minha_carteira_view(request):
    return render(request, "financas/carteira.html") 

def dashboard(request):
    return render(request, "financas/dashboard.html") 
