from django.shortcuts import render

#Renderiza a página html que será acessada mediante uma requisição
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contato.html')
