from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User

# Formulário de login customizado
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Email ou telefone",
        widget=forms.TextInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Email ou telefone',
        })
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Senha',
        })
    )

# Formulário de cadastro customizado
class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=100,
        required=True,
        label="Nome Completo",
        widget=forms.TextInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Nome completo'
        })
    )
    email = forms.EmailField(
        required=True,
        label="Seu Melhor E-mail",
        widget=forms.EmailInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'E-mail'
        })
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        label="Telefone",
        widget=forms.TextInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Telefone'
        })
    )
    password1 = forms.CharField(
        label="Criar Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Senha'
        })
    )
    password2 = forms.CharField(
        label="Repetir Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Confirme a senha'
        })
    )

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone', 'password1', 'password2']

# Formulário de reset de senha
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Digite seu email',
        })
    )

# Formulário de definir nova senha
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Nova senha',
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Confirme a nova senha',
        })
    )