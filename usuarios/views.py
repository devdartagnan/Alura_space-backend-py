from django.shortcuts import render,redirect
from usuarios.forms import LoginForms, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form  = LoginForms(request.POST)
        
        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()
            
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request,usuario)
            messages.success(request, f"{nome}, você está logado!")
            return redirect('index')
        else:
            messages.error(request, 'Algum erro aconteceu, cheque suas informações')
            return redirect('login')
    
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForm()
    
    if request.method == 'POST':
        form  = CadastroForm(request.POST)
        
        if form.is_valid():
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'O email já existe')
                return redirect('cadastro')
        
            usuario = User.objects.create_user(
                username=nome,
                email=email ,
                password=senha
                )
            
            usuario.save()
            messages.success(request, f"{nome}, você foi cadastrado")
            return redirect('login')
            
    return render(request, 'usuarios/cadastro.html', {'form': form})


def logout(request):
    messages.success(request, "Logout efetuado com sucesso!")
    auth.logout(request)
    return redirect('login')