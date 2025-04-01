from django.db import models

class Setor(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)


    class Meta:
        verbose_name = "Setor"
        verbose_name_plural ="Setores"

    def __str__(self):
        return self.nome



class Cargo(models.Model):
    nome =models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    nivel_hierarquico = models.CharField(max_length=50, choices=[("junior","junior"),
                                                                 ("Pleno","Pleno"),
                                                                 ("Senior","Sennior"),
                                                                 ("Lideranca","Lideranca"),],
                                                                 default="Junior"
                                                                 )




    class Meta:
        verbose_name ="Cargo"
        verbose_name_plural ="Cargos"


    def __str__(self):
        return self.nome



class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_admissao = models.DateField()
    setor = models.ForeignKey(Setor, on_delete=models.SET_DEFAULT, null=True, verbose_name="Setor")
    cargo = models.ForeignKey(Cargo,on_delete=models.SET_DEFAULT, null=True, verbose_name ="Cargo")
    Salario_atual = models.DecimalField(max_digits=10, decimal_places=2) 
    foto = models.ImageField(upload_to="foto_funcionarios/", blank=True, null=True)


    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
