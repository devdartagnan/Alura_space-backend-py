from django.shortcuts import render, get_object_or_404, redirect
from apps.gallery.models import Cards
from apps.gallery.forms import CardsForms
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    dados = Cards.objects.order_by('data_card').filter(publicado=True)
    return render(request, 'gallery/index.html', {'cards': dados})

def imagem(request, foto_id):
    card = get_object_or_404(Cards, pk=foto_id)
    return render(request, 'gallery/imagem.html', { 'cards' : card })

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    dados = Cards.objects.order_by('data_card').filter(publicado=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            dados = dados.filter(nome__icontains=nome_a_buscar)
            
    return render (request, "gallery/index.html", {'cards': dados})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    form = CardsForms
    if request.method == 'POST':
        form = CardsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')
        
    return render (request, 'gallery/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    card = Cards.objects.get(id=foto_id)
    form = CardsForms(instance=card)
    
    if request.method == 'POST':
        form = CardsForms(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            messages.info(request, 'Fotografia editada com sucesso!')
            return redirect ('index')   
    
    return render(request,'gallery/editar_imagem.html', {'form': form, 'foto_id': foto_id})


def deletar_imagem(request, foto_id):
    card = Cards.objects.get(id=foto_id)
    card.delete()
    messages.success(request, 'A imagem foi apagada!')
    return redirect('index')

def filtro(request, categoria):
    categoria = Cards.objects.filter(publicado=True, categoria=categoria)
    
    return render(request,'gallery/index.html',{'cards': categoria})