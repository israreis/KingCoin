from django.urls import path
from .views import (
    landing,
    CustomLoginView,
    CustomLogoutView,
    RegisterView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    minha_carteira_view
)
from django.contrib.auth import views as auth_views

# A linha 'app_name = "financas"' foi removida daqui.

urlpatterns = [
    # Página inicial
    path("", landing, name="landing"),

    # Autenticação
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),

    # Recuperação de senha
    path(
        "password-reset/",
        CustomPasswordResetView.as_view(),
        name="password_reset"
    ),

    # Confirmação de envio do link
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="financas/password_reset_done.html"
        ),
        name="password_reset_done"
    ),

    # Redefinição de senha via link
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),

    # Nova URL da Carteira
    path('minha-carteira/', minha_carteira_view, name='minha-carteira'),
]