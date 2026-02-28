
from django.shortcuts import render
from .models import Filme # Importa a nova classe

def index(request):
    # Busca todos os filmes salvos no banco de dados
    filmes = Filme.objects.all()
    # Passa os filmes para o HTML através do dicionário 'contexto'
    return render(request, 'index.html', {'lista_filmes': filmes})