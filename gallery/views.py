from django.shortcuts import render, get_object_or_404, redirect
from gallery.models import Cards
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
            
    return render (request, "gallery/buscar.html", {'cards': dados})