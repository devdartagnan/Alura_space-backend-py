from django.shortcuts import render, get_object_or_404
from gallery.models import Cards

def index(request):
    dados = Cards.objects.order_by('data_card').filter(publicado=True)
    return render(request, 'gallery/index.html', {'cards': dados})

def imagem(request, foto_id):
    card = get_object_or_404(Cards, pk=foto_id)
    return render(request, 'gallery/imagem.html', { 'cards' : card })

def buscar(request):
    dados = Cards.objects.order_by('data_card').filter(publicado=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            dados = dados.filter(nome__icontains=nome_a_buscar)
            
    return render (request, "gallery/buscar.html", {'cards': dados})