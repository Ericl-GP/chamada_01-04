from django import forms
from chamadaApp.models import *

class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'

class CategoriaFom(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class PlanoFom(forms.ModelForm):
    class Meta:
        model = Plano
        fields = '__all__'

class ClienteFom(forms.ModelForm):
    class Meta:
        model = Cliente
        fields ='__all__'
