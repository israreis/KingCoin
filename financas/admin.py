# financas/admin.py - PERSONALIZAÇÃO OPCIONAL
from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('financas')

for model_name, model in app.models.items():
    try:
        if model_name == 'movimentacao':
            @admin.register(model)
            class MovimentacaoAdmin(admin.ModelAdmin):
                list_display = ['id_movimentacao', 'usuario', 'data_formatada', 'valor', 'categoria', 'tipo_movimentacao']
                list_filter = ['categoria__tipoMovimentacao', 'data_movimentacao']
                search_fields = ['descricao', 'usuario__username']
                date_hierarchy = 'data_movimentacao'
                
                def data_formatada(self, obj):
                    return obj.data_movimentacao.strftime('%d/%m/%Y')
                data_formatada.short_description = 'Data Movimentação'
        else:
            admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass