from django import forms

class LoginForms(forms.Form):
    nome_login =forms.CharField(
        label='Nome de login',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        ),
        required=True
        )
    senha =forms.CharField(
        label='Senha',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
        required=True
        )
    
class CadastroForm(forms.Form):
    nome_cadastro =forms.CharField(
        label='Nome de login',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        ),
        required=True
        )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu Email',
            }
        ),
        required=True
    )
    senha_1 =forms.CharField(
        label='Senha',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
        required=True
        )
    senha_2 =forms.CharField(
        label='Confirmação de senha',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente',
            }
        ),
        required=True
        )
    