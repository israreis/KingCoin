from django.urls import path
from .views import (
    landing,
    sidebar,
    sidebar2,
    CustomLoginView,
    CustomLogoutView,
    RegisterView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,  # view customizada para redefinir senha
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Página inicial
    path("", landing, name="landing"), 
    path("sidebar/", sidebar, name='sidebar'),
    path("sidebar2/", sidebar2, name='sidebar2'),
     

    # Autenticação
    path("login/", CustomLoginView.as_view(), name="login"),     
    path("logout/", CustomLogoutView.as_view(), name="logout"),   
    path("register/", RegisterView.as_view(), name="register"),
   

    # Recuperação de senha usando a view customizada
    path(
        "password-reset/",
        CustomPasswordResetView.as_view(),
        name="password_reset"
    ),

    # Página de confirmação de envio do link
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="financas/password_reset_done.html"
        ),
        name="password_reset_done"
    ),

    # Página de redefinição de senha via link usando view customizada
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),

]
