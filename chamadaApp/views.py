from django.shortcuts import render

# Create your views here.

def index(reguest):
    return render(reguest, 'chamada/new_cliente.html')