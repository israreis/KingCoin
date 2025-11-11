from django.contrib.auth.models import User
from django.db import models
import os

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Telefone"
    )
    photo = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True,
        verbose_name="Foto de perfil"
    )
    
    def __str__(self):
        return f"Perfil de {self.user.email}"
    
    def delete(self, *args, **kwargs):
        # Deleta a foto do sistema de arquivos quando o perfil é deletado
        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)
        super().delete(*args, **kwargs)

#TipoMovimentação (enumeration)
class TipoMovimentacao(models.Model):
    TIPO_CHOICES = [
        ('RECEITA', 'Receita'),
        ('DESPESA', 'Despesa'),
        ('ECONOMIA', 'Economia'),
    ]
    
    nome = models.CharField(max_length=50, choices=TIPO_CHOICES, unique=True)
    
    def __str__(self):
        return self.get_nome_display()
    

#TipoPercentual (enumeration)
class TipoPercentual(models.Model):
    TIPO_CHOICES = [
        ('NECESSIDADES', 'Necessidades'),
        ('DESEJOS', 'Desejos'),
        ('POUPANCA', 'Poupança'),
    ]
    
    nome = models.CharField(max_length=50, choices=TIPO_CHOICES, unique=True)
    
    def __str__(self):
        return self.get_nome_display()        
    

#Categoria (enumeration)
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nomeCategoria = models.CharField(max_length=100)
    tipoMovimentacao = models.ForeignKey(TipoMovimentacao, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    @classmethod
    def categorias_por_tipo(cls, tipo_nome):
        """Retorna categorias filtradas por tipo de movimentação"""
        return cls.objects.filter(tipoMovimentacao__nome=tipo_nome)
    
    def __str__(self):
        return self.nomeCategoria


# Movimentacao - MODELO CORRIGIDO
class Movimentacao(models.Model):
    id_movimentacao = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_movimentacao = models.DateField()  
    criado_em = models.DateTimeField(auto_now_add=True) 
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'
        ordering = ['-data_movimentacao']  
    
    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"
    
    def tipo_movimentacao(self):
        return self.categoria.tipoMovimentacao
    tipo_movimentacao.short_description = 'Tipo'

    def get_icon_class(self):
        """Retorna classe do ícone baseado na categoria"""
        icons = {
            'Salário': 'fa-money-bill-wave',
            'Freelance': 'fa-laptop-code',
            'Aluguel': 'fa-house-user',
            'Supermercado': 'fa-shopping-basket',
            'Transporte': 'fa-bus',
            'Saúde': 'fa-hospital-user',
            'Lazer': 'fa-face-laugh-beam',
            'Restaurante': 'fa-utensils',
            'Educação': 'fa-graduation-cap',
            'Poupança': 'fa-piggy-bank',
            'Investimentos': 'fa-chart-line',
            'Moradia': 'fa-home',
            'Alimentação': 'fa-utensils',
            'Outros Rendimentos': 'fa-money-bill',
            'Outros gastos': 'fa-receipt',
        }
        return icons.get(self.categoria.nomeCategoria, 'fa-receipt')
    
    def get_icon_color(self):
        """Retorna cor do ícone baseado no tipo"""
        colors = {
            'RECEITA': '#23b785',
            'DESPESA': '#ff6b6b', 
            'ECONOMIA': '#9b59b6',
        }
        return colors.get(self.categoria.tipoMovimentacao.nome, '#6c757d')    

    @property
    def tipoMovimentacao(self):
        return self.categoria.tipoMovimentacao