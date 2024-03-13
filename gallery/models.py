from django.db import models
from datetime import datetime

class Cards(models.Model):
    LISTA_DE_CATEGORIAS = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]
    
    nome = models.CharField(max_length=100, null= False, blank=False)
    legenda = models.CharField(max_length=150, null= False, blank=False)
    categoria = models.CharField(max_length=100,choices=LISTA_DE_CATEGORIAS, default='')
    descricao = models.TextField(null= False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicado = models.BooleanField(default=False)
    data_card = models.DateTimeField(default=datetime.now)  #cria
    
    
    def __str__(self):
        return self.nome