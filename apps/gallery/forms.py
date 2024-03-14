from django import forms

from apps.gallery.models import Cards

class CardsForms(forms.ModelForm):
    class Meta():
        model = Cards
        exclude = ['publicado',]
        labels = {
            'descricao': 'Descrição',
            'data_card': 'Data da publicação',
            'usuario': 'Usuário'
        }
        
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}), 
            'legenda':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'descricao':forms.TextInput(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class':'form-control'}), 
            'data_card': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'usuario':forms.Select(attrs={'class':'form-control'}),
        }