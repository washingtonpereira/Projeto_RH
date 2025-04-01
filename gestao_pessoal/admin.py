from django.contrib import admin

from .models import Setor, Cargo, Funcionario

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)
    ordering = ('nome',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_hierarquico', 'descricao')
    list_filter = ('nivel_hierarquico',)
    search_fields = ('nome',)
    ordering = ('nome',)

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'telefone', 'setor', 'cargo', 'data_admissao', 'salario_atual')
    list_filter = ('setor', 'cargo', 'data_admissao')
    search_fields = ('nome', 'sobrenome', 'email')
    ordering = ('nome', 'sobrenome')
    fieldsets = (
   ('Informações Pessoais', {
            'fields': ('nome', 'sobrenome', 'email', 'telefone')
        }),
        ('Informações Profissionais', {
            'fields': ('setor', 'cargo', 'data_admissao')
        }),
        ('Detalhes Financeiros', {
            'fields': ('salario_atual',)
        }),
    )
    def nome_completo(self, obj):
        return f"{obj.nome} {obj.sobrenome}"
    nome_completo.short_description = 'Nome Completo'
