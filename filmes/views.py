from django.shortcuts import render, redirect # Adicione o redirect aqui
from .models import Filme
from .forms import FilmeForm # Importe o form que criamos acima
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    filmes = Filme.objects.all()
    return render(request, 'index.html', {'lista_filmes': filmes})

# ADICIONE ESTA FUNÇÃO NOVA:
def novo_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save() # Salva no MySQL automaticamente
            return redirect('index') # Volta para a lista após salvar
    else:
        form = FilmeForm()
    return render(request, 'cadastrar.html', {'form': form})

def editar_filme(request, id):
    filme = get_object_or_404(Filme, id=id)
    # O 'instance=filme' preenche o formulário com os dados atuais do filme
    form = FilmeForm(request.POST or None, instance=filme)
    
    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request, 'cadastrar.html', {'form': form, 'editando': True})

def excluir_filme(request, id):
    filme = get_object_or_404(Filme, id=id)
    filme.delete() # Remove do MySQL
    return redirect('index')