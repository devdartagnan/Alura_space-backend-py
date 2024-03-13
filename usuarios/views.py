from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForm

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})
