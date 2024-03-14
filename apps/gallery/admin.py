from django.contrib import admin 
from apps.gallery.models import Cards

class ListandoCards(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicado', 'data_card', 'usuario') 
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')
    list_filter = ('categoria','usuario')
    list_editable = (('publicado'), )
    list_per_page = 10

admin.site.register(Cards, ListandoCards)

