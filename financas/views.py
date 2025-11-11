from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Sum, Q
from decimal import Decimal
from .models import Profile
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Movimentacao, Categoria, TipoMovimentacao
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required 
from .forms import (
    CustomLoginForm,
    CustomUserCreationForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
    ProfileForm  
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
                    
                    # Redireciona para a página de confirmação
                    return render(request, 'financas/register_done.html')
                    
            except IntegrityError as e:
                form.add_error('email', 'Erro ao criar conta. Este e-mail já pode estar em uso.')
                print(f"Erro de integridade: {e}")
                
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'financas/register.html', {'form': form})


def register_done(request):
    return render(request, 'financas/register_done.html')

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
@login_required
def transacoes(request):
    """View para a página de Transações"""
    # Busca todas as transações do usuário ordenadas por data
    todas_transacoes = Movimentacao.objects.filter(
        usuario=request.user
    ).select_related('categoria', 'categoria__tipoMovimentacao').order_by('-data_movimentacao')
    
    # Agrupa transações por data
    transacoes_por_data = {}
    for transacao in todas_transacoes:
        data_str = transacao.data_movimentacao.strftime('%Y-%m-%d')
        if data_str not in transacoes_por_data:
            transacoes_por_data[data_str] = []
        transacoes_por_data[data_str].append(transacao)
    
    context = {
        'transacoes_por_data': transacoes_por_data,
        'todas_transacoes': todas_transacoes
    }
    return render(request, 'financas/transacoes.html', context)

@login_required
def minha_carteira_view(request):
    periodo = request.GET.get('periodo', 'este_mes')
    
    # Buscar transações do período
    data_inicio, data_fim = calcular_periodo(periodo)
    
    transacoes_periodo = Movimentacao.objects.filter(
        usuario=request.user,
        data_movimentacao__gte=data_inicio,
        data_movimentacao__lte=data_fim
    ).select_related('categoria', 'categoria__tipoMovimentacao').order_by('-data_movimentacao')[:10]  # Limita para performance
    
    # Últimas transações (últimos 30 dias)
    data_limite_transacoes = timezone.now().date() - timedelta(days=30)
    ultimas_transacoes = Movimentacao.objects.filter(
        usuario=request.user,
        data_movimentacao__gte=data_limite_transacoes
    ).select_related('categoria', 'categoria__tipoMovimentacao').order_by('-data_movimentacao')[:5]
    
    # Calcular totais
    saldo_info = calcular_saldo_usuario(request.user, periodo)
    investimentos_info = calcular_investimentos_usuario(request.user, periodo)
    
    # Buscar categorias para os modais
    categorias_receita = Categoria.categorias_por_tipo('RECEITA')
    categorias_despesa = Categoria.categorias_por_tipo('DESPESA') 
    categorias_economia = Categoria.categorias_por_tipo('ECONOMIA')
    
    # Datas para templates
    hoje = timezone.now().date()
    ontem = hoje - timedelta(days=1)
    
    context = {
        'transacoes_periodo': transacoes_periodo,
        'ultimas_transacoes': ultimas_transacoes,
        'saldo': saldo_info['saldo'],
        'saldo_variacao': saldo_info['variacao'],
        'saldo_porcentagem': saldo_info['porcentagem'],
        'investimentos': investimentos_info['valor'],
        'invest_variacao': investimentos_info['variacao'],
        'invest_porcentagem': investimentos_info['porcentagem'],
        'periodo_selecionado': periodo,
        'data_hoje': hoje.strftime('%Y-%m-%d'),
        'data_ontem': ontem.strftime('%Y-%m-%d'),
        'periodo_texto': obter_texto_periodo(periodo),
        'categorias_receita': categorias_receita,
        'categorias_despesa': categorias_despesa,
        'categorias_economia': categorias_economia,
    }
    return render(request, 'financas/carteira.html', context)

def obter_texto_periodo(periodo):
    textos = {
        'este_mes': 'Este mês',
        'ultimo_mes': 'Último mês', 
        'ultimos_3_meses': 'Últimos 3 meses'
    }
    return textos.get(periodo, 'este mês')


# Funções auxiliares
def calcular_periodo(periodo):
    """Calcula as datas de início e fim baseado no período selecionado"""
    hoje = timezone.now().date()
    
    if periodo == 'este_mes':
        data_inicio = hoje.replace(day=1)
        data_fim = hoje
    elif periodo == 'ultimo_mes':
        primeiro_dia_mes_atual = hoje.replace(day=1)
        data_fim = primeiro_dia_mes_atual - timedelta(days=1)
        data_inicio = data_fim.replace(day=1)
    elif periodo == 'ultimos_3_meses':
        data_fim = hoje
        data_inicio = hoje - timedelta(days=90)
    else:  # default: este mês
        data_inicio = hoje.replace(day=1)
        data_fim = hoje
    
    return data_inicio, data_fim

def calcular_saldo_usuario(usuario, periodo):
    """Calcula saldo, variação e porcentagem para o período do usuário"""
    data_inicio, data_fim = calcular_periodo(periodo)
    
    # Buscar período anterior para comparação
    if periodo == 'este_mes':
        periodo_anterior = 'ultimo_mes'
    elif periodo == 'ultimo_mes':
        periodo_anterior = 'ultimos_3_meses'
    else:  # últimos 3 meses
        periodo_anterior = 'ultimo_mes'
    
    data_inicio_anterior, data_fim_anterior = calcular_periodo(periodo_anterior)
    
    # Calcular saldo atual
    receitas_atual = Movimentacao.objects.filter(
        usuario=usuario,
        data_movimentacao__gte=data_inicio,
        data_movimentacao__lte=data_fim,
        categoria__tipoMovimentacao__nome='RECEITA'
    ).aggregate(total=Sum('valor'))['total'] or Decimal('0')
    
    despesas_atual = Movimentacao.objects.filter(
        usuario=usuario,
        data_movimentacao__gte=data_inicio,
        data_movimentacao__lte=data_fim,
        categoria__tipoMovimentacao__nome='DESPESA'
    ).aggregate(total=Sum('valor'))['total'] or Decimal('0')
    
    saldo_atual = receitas_atual - despesas_atual
    
    # Calcular saldo período anterior
    receitas_anterior = Movimentacao.objects.filter(
        usuario=usuario,
        data_movimentacao__gte=data_inicio_anterior,
        data_movimentacao__lte=data_fim_anterior,
        categoria__tipoMovimentacao__nome='RECEITA'
    ).aggregate(total=Sum('valor'))['total'] or Decimal('0')
    
    despesas_anterior = Movimentacao.objects.filter(
        usuario=usuario,
        data_movimentacao__gte=data_inicio_anterior,
        data_movimentacao__lte=data_fim_anterior,
        categoria__tipoMovimentacao__nome='DESPESA'
    ).aggregate(total=Sum('valor'))['total'] or Decimal('0')
    
    saldo_anterior = receitas_anterior - despesas_anterior
    
    # Calcular variação
    if saldo_anterior != 0:
        variacao_valor = saldo_atual - saldo_anterior
        variacao_porcentagem = (variacao_valor / abs(saldo_anterior)) * 100
    else:
        variacao_valor = saldo_atual
        variacao_porcentagem = 100 if saldo_atual > 0 else -100 if saldo_atual < 0 else 0
    
    return {
        'saldo': saldo_atual,
        'variacao': variacao_valor,
        'porcentagem': variacao_porcentagem
    }

def calcular_investimentos_usuario(usuario, periodo):
    """Calcula investimentos, variação e porcentagem para o período do usuário"""
    data_inicio, data_fim = calcular_periodo(periodo)
    
    # Buscar período anterior para comparação
    if periodo == 'este_mes':
        periodo_anterior = 'ultimo_mes'
    elif periodo == 'ultimo_mes':
        periodo_anterior = 'ultimos_3_meses'
    else:
        periodo_anterior = 'ultimo_mes'
    
    data_inicio_anterior, data_fim_anterior = calcular_periodo(periodo_anterior)
    
    # Calcular investimentos atual
    investimentos_atual = Movimentacao.objects.filter(
        usuario=usuario,
        data_movimentacao__gte=data_inicio,
        data_movimentacao__lte=data_fim,
        categoria__tipoMovimentacao__nome='ECONOMIA'
    ).aggregate(total=Sum('valor'))['total'] or Decimal('0')
    
    # Calcular investimentos período anterior
    investimentos_anterior = Movimentacao.objects.filter(
        usuario=usuario,
        data_movimentacao__gte=data_inicio_anterior,
        data_movimentacao__lte=data_fim_anterior,
        categoria__tipoMovimentacao__nome='ECONOMIA'
    ).aggregate(total=Sum('valor'))['total'] or Decimal('0')
    
    # Calcular variação
    if investimentos_anterior != 0:
        variacao_valor = investimentos_atual - investimentos_anterior
        variacao_porcentagem = (variacao_valor / abs(investimentos_anterior)) * 100
    else:
        variacao_valor = investimentos_atual
        variacao_porcentagem = 100 if investimentos_atual > 0 else -100 if investimentos_atual < 0 else 0
    
    return {
        'valor': investimentos_atual,
        'variacao': variacao_valor,
        'porcentagem': variacao_porcentagem
    }

@login_required
def dashboard(request):
    return render(request, "financas/dashboard.html")

@login_required  
def relatorios(request):
    return render(request, "financas/relatorios.html")



@login_required
def minha_conta(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Atualiza o perfil
            form.save()
            
            # Atualiza os dados do usuário
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('minha-conta')
    else:
        # Preenche o formulário com os dados atuais
        form = ProfileForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'phone': profile.phone,
        })
    
    return render(request, 'financas/minha_conta.html', {
        'form': form,
        'profile': profile
    })


#Views de finanças

@login_required
def get_categorias_por_tipo(request, tipo_nome):
    """Retorna categorias filtradas por tipo"""
    categorias = Categoria.categorias_por_tipo(tipo_nome)
    categorias_list = [
        {'id': cat.id_categoria, 'nome': cat.nomeCategoria}
        for cat in categorias
    ]
    return JsonResponse({'categorias': categorias_list})

@csrf_exempt
@require_http_methods(["POST"])
@login_required
def criar_movimentacao(request):
    """Cria uma nova movimentação"""
    try:
        data = json.loads(request.body)
        
        movimentacao = Movimentacao(
            usuario=request.user,
            data_movimentacao=datetime.strptime(data['data'], '%Y-%m-%d').date(),
            valor=data['valor'],
            descricao=data['descricao'],
            categoria_id=data['categoria_id']
        )
        movimentacao.save()
        
        return JsonResponse({
            'success': True, 
            'message': 'Movimentação criada com sucesso!',
            'id': movimentacao.id_movimentacao
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': f'Erro ao criar movimentação: {str(e)}'
        }, status=400)


