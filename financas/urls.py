from django.urls import path
from .views import (  # <-- importando corretamente das views
    landing,
    transacoes,
    CustomLoginView,
    CustomLogoutView,
    RegisterView,
    register_done,
    minha_conta,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    minha_carteira_view,
    dashboard,
    relatorios,
    get_categorias_por_tipo,
    criar_movimentacao
)
from django.contrib.auth import views as auth_views

# A linha 'app_name = "financas"' foi removida daqui.

urlpatterns = [
    # Página inicial
    path("", landing, name="landing"),

    path("transacoes/", transacoes, name="transacoes"),

    # Autenticação
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterView, name="register"),
    path("register_done", register_done, name="register_done"),

    # Recuperação de senha
    path(
        "password-reset/",
        CustomPasswordResetView.as_view(),
        name="password_reset",
    ),

    # Confirmação de envio do link
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="financas/password_reset_done.html"
        ),
        name="password_reset_done",
    ),

    # Redefinição de senha via link
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    
    # Minha conta 
    path('minha-conta/', minha_conta, name='minha-conta'),

    # Nova URL da Carteira
    path('minha-carteira/', minha_carteira_view, name='minha-carteira'),

     # Nova URL da dashboard
    path('dashboard/', dashboard, name='dashboard'),

         # Nova URL da relatorios
    path('relatorios/', relatorios, name='relatorios'),



    path('api/categorias/<str:tipo_nome>/', get_categorias_por_tipo, name='get_categorias_por_tipo'),
    path('api/movimentacoes/criar/', criar_movimentacao, name='criar_movimentacao'),
    
]