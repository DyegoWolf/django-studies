from django.shortcuts import render

#Renderiza a página html que será acessada mediante uma requisição
def index(request):
    context = {
        'nome': 'Dyego',
    }

    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contato.html')
