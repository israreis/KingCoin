from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
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

# --- Registro ---
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "financas/register.html"
    success_url = reverse_lazy("landing")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

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
