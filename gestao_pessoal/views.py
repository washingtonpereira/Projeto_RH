from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')


def listar(request):
    return render(request, 'lista.hrml')