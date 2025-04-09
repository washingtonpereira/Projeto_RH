# Projeto RH

Software de Gestão de Recursos Humanos desenvolvido em Python, utilizando o framework Django.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Sobre o Projeto

O Projeto RH é uma aplicação web para gerenciar informações de recursos humanos, permitindo o cadastro, edição e visualização de dados de funcionários e departamentos.

## Funcionalidades

- **Gestão de Pessoal**: Cadastro e gerenciamento de funcionários.
- **Gestão de Departamentos**: Administração dos departamentos da empresa.
- **Relatórios**: Geração de relatórios relacionados aos recursos humanos.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework**: Django
- **Banco de Dados**: SQLite (padrão do Django, pode ser alterado conforme necessidade)
- **Front-end**: HTML, CSS e JavaScript

## 🧠 Mapa Mental do Sistema de RH

O diagrama no link abaixo diagrama resume a estrutura geral do sistema e suas funcionalidades principais.


[Ver Mapa Mental do Sistema](https://raw.githubusercontent.com/washingtonpereira/Projeto_RH/main/docs/mapa_mental_sistema.jpg)

## Instalação

 **Clone o repositório**:

   bash
   git clone https://github.com/washingtonpereira/Projeto_RH.git

   # Crie e ative um ambiente virtual

## Como Usar
python -m venv venv
venv\Scripts\activate  # No Windows
# ou
source venv/bin/activate  # No Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Realize as migrações
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver



## 🤝 Contribuição

Contribuições são bem-vindas! Se você quiser melhorar algo, siga os passos abaixo:

1. Faça um fork do projeto
2. Crie uma branch para sua feature:
   
   git checkout -b minha-nova-feature

   git commit -m 'Adiciona nova funcionalidade'

   git push origin minha-nova-feature



## 📬 Contato 

Se tiver dúvidas, sugestões ou quiser trocar uma ideia:

**Washington Luis de Assis Pereira**  
📍 Niterói - RJ  
📧 slash.o.teobaldo@gmail.com  
🔗 [GitHub](https://github.com/washingtonpereira)
