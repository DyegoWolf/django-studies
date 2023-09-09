from django.shortcuts import render

#Renderiza a página html que será acessada mediante uma requisição
def index(request):

    # Verifica se o usuário está logado
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = "Usuário logado"

    context = {
        'nome': 'Dyego',
        'logado': teste
    }

    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contato.html')
