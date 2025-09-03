from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import CustomLoginForm, CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = "financas/login.html"
    authentication_form = CustomLoginForm


class CustomLogoutView(LogoutView):
    # redireciona para a landing após logout
    next_page = reverse_lazy("landing")


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "financas/register.html"
    # redireciona para a landing após cadastro
    success_url = reverse_lazy("landing")

    def form_valid(self, form):
        # salva o usuário
        user = form.save()
        # loga automaticamente após cadastro
        login(self.request, user)
        return super().form_valid(form)


def landing(request):
    return render(request, "financas/landing.html")
