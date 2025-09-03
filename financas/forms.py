from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-full bg-black/40 border border-white/20 text-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400',
            'placeholder': 'Usuário ou E-mail'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 rounded-full bg-black/40 border border-white/20 text-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400',
            'placeholder': 'Senha'
        })
    )

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nome",
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-full bg-black/40 border border-white/20 text-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400',
            'placeholder': 'Nome'
        })
    )
    last_name = forms.CharField(
        label="Sobrenome",
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-full bg-black/40 border border-white/20 text-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400',
            'placeholder': 'Sobrenome'
        })
    )

    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 rounded-full bg-black/40 border border-white/20 text-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400',
            'placeholder': 'Senha'
        })
    )
    password2 = forms.CharField(
        label="Confirmação de senha",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 rounded-full bg-black/40 border border-white/20 text-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400',
            'placeholder': 'Confirmar senha'
        })
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
        widgets = {
            "username": forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-full bg-black/40 border border-white/20 text-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400',
                'placeholder': 'Nome de usuário'
            }),
            "email": forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 rounded-full bg-black/40 border border-white/20 text-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-400',
                'placeholder': 'E-mail'
            }),
        }