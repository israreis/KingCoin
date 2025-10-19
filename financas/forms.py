from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User

# Formulário de login customizado
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Seu email",
        widget=forms.TextInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Seu email',
        })
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Senha',
        })
    )

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        label="Nome",
        widget=forms.TextInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Nome'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        label="Sobrenome",
        widget=forms.TextInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Sobrenome'
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
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        
        # Verifica se o email também existe no campo email (para consistência)
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        
        return cleaned_data

# Formulário de reset de senha
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Seu email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Digite seu email',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Seu email"

# Formulário de definir nova senha
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Nova senha",
        widget=forms.PasswordInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Nova senha',
        })
    )
    new_password2 = forms.CharField(
        label="Confirmar nova senha",
        widget=forms.PasswordInput(attrs={
            'class': 'bg-transparent border-b border-gray-500 w-full py-2 focus:outline-none focus:border-[#23b785]',
            'placeholder': 'Confirme a nova senha',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].label = "Nova senha"
        self.fields['new_password2'].label = "Confirmar nova senha"