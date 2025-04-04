from django import forms
from .models import Setor, Cargo, Funcionario


class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields =["nome","descricao"]




class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ["nome","Descricao","nivel_hierarquico"]


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ["nome",
                 "sobrenome",
                 "email",
                 "telefone",
                 "data_admissao",
                 "setor",
                 "cargo",
                 "salario_atual"]
