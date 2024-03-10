from django.urls import path
from gallery.views import index
from gallery.views import imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem')
]
